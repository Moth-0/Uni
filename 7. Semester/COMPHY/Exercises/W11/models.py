import torch 
import torch.nn as nn
import torch.optim as optim
import copy
from torch.utils.data import Dataset, DataLoader


class LinearModel(nn.Module):
    def __init__(self, *args, bias=True, **kwargs):
        super().__init__(*args, **kwargs)
        self.layer1 = nn.Linear(1, 1, bias=bias)
        self.is_fitted = False

    def forward(self, x):
        x = x.view(-1, 1)
        x = self.layer1(x)
        return x.flatten()

    def fit(self, xs, ys, epochs=500, lr=0.1,
            lossFunction=nn.MSELoss, optimizer=optim.Adam):
        
        self.lossFunc = lossFunction()
        self.optimizer = optimizer(self.parameters(), lr=lr)

        for _ in range(epochs):
            self.optimizer.zero_grad()
            pred = self(xs)
            loss = self.lossFunc(pred, ys)
            loss.backward()
            self.optimizer.step()

        self.is_fitted = True
        # Wack way -_-
        return tuple(map(lambda p: p.item(), self.parameters()))

    def plot(self, ax, xs, ys):
            if not self.is_fitted:
                raise RuntimeError("The model must be fitted before plotting.")
    
            # Plot original data points saved during fit()
            ax.scatter(xs.numpy(), ys.numpy(), color='red', label='Data points')
    
            x_vals = torch.linspace(min(xs), max(xs), 1000).view(-1, 1)
            y_preds = self(x_vals).detach().numpy()
    
            label = f'Fitted line'
    
            ax.plot(x_vals.numpy(), y_preds, color='blue', label=label)
    
            ax.axhline(0, color='black', linewidth=0.5)
            ax.axvline(0, color='black', linewidth=0.5)
            ax.legend()
            ax.grid()
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_title(f'Fitting with {self._get_name()}')

class LinearSiLUModule(nn.Module):
    def __init__(self, *args, hidden=4, layers=0, **kwargs):
        '''
        uses 1 -> N -> N -> ... -> 1
        with linear and and SiLU at each node  
        N is the number of hidden nodes (default 4). 
        1 -> N -> 1 is layers=0, which is default. 
        '''
        super().__init__(*args, **kwargs)

        self.layers = nn.ModuleList([nn.Linear(1,hidden), nn.SiLU()])

        for _ in range(layers):
            self.layers.append(nn.Linear(hidden, hidden))
            self.layers.append(nn.SiLU())

        self.layers.append(nn.Linear(hidden, 1))

        self.is_fitted = False

    def forward(self, x):
        x = x.view(-1, 1)
        for layer in self.layers:
            x = layer(x)
        return x.flatten()

    def fit(self, xs, ys, epochs=500, lr=0.1,
            lossFunction=nn.MSELoss, optimizerFunc=optim.Adam, weight_decay=0.0):
        
        self.lossFunc = lossFunction()
        self.optimizer = optimizerFunc(self.parameters(), lr=lr, weight_decay=weight_decay)

        for _ in range(epochs):
            self.optimizer.zero_grad()
            pred = self(xs)
            loss = self.lossFunc(pred, ys)
            loss.backward()
            self.optimizer.step()

        self.is_fitted = True
        return tuple(self.parameters())

    def plot(self, ax, xs, ys):
        if not self.is_fitted:
            raise RuntimeError("The model must be fitted before plotting.")

        # Plot original data points saved during fit()
        ax.scatter(xs.numpy(), ys.numpy(), color='red', label='Data points')

        x_vals = torch.linspace(xs.min().item(), xs.max().item(), 1000).view(-1, 1)        
        y_preds = self(x_vals).detach().numpy()

        label = f'Loss = {self.lossFunc(self(xs), ys):.2f}'

        ax.plot(x_vals.numpy(), y_preds, color='blue', label=label)

        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.legend()
        ax.grid()
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title(f'Fitting with {self._get_name()}')

class XDLinearModel(nn.Module):
    def __init__(self, in_dim, out_dim, hidden=None, layers=0, bias=True, *args, **kwargs):
        '''
        uses in_dim -> N -> N -> ... -> out_dim
        with linear and and SiLU at each node (no SiLu on output)
        N is the number of hidden nodes (default 4). 
        1 -> N -> 1 is layers=0, which is default. 
        '''
        super().__init__(*args, **kwargs)
        
        self.in_dim = in_dim
        self.out_dim = out_dim
        self.hidden = hidden if hidden is not None else in_dim
        self.is_fitted = False
        
        self.net = nn.ModuleList()
        
        if layers == 0:
            self.net.append(nn.Linear(self.in_dim, self.out_dim, bias=bias))
        else:
            self.net.append(nn.Linear(self.in_dim, self.hidden, bias=bias))
            self.net.append(nn.SiLU())
            
            for _ in range(layers - 1):
                self.net.append(nn.Linear(self.hidden, self.hidden, bias=bias))
                self.net.append(nn.SiLU())
                
            self.net.append(nn.Linear(self.hidden, self.out_dim, bias=bias))

    def forward(self, x):
        x = x.view(-1, self.in_dim)
        for layer in self.net:
            x = layer(x)
            
        if self.out_dim == 1:
            return x.flatten()
        return x

    def fit(self, xs, ys, epochs=500, lr=0.1, lossFunction=nn.MSELoss, optimizerFunc=optim.Adam):
        self.lossFunc = lossFunction()
        self.optimizer = optimizerFunc(self.parameters(), lr=lr)

        for _ in range(epochs):
            self.optimizer.zero_grad()
            pred = self(xs)
            loss = self.lossFunc(pred, ys)
            loss.backward()
            self.optimizer.step()

        self.is_fitted = True
        return tuple(self.parameters())

def fit_model(
    model,
    train_loader,
    criterion=nn.MSELoss(),
    optimizer_class=optim.Adam,
    lr=1e-3,
    weight_decay=0.0,
    val_loader=None,
    test_loader=None,
    epochs=100,
    patience=None,
    device=None
):
    """
    A generic PyTorch training loop with built-in validation, early stopping, and test evaluation.
    
    Args:
        model: PyTorch nn.Module.
        train_loader: DataLoader for training data.
        criterion: Loss function (e.g., nn.MSELoss()).
        optimizer_class: Optimizer class (uninstantiated), defaults to Adam.
        lr: Learning rate.
        weight_decay: L2 penalty.
        val_loader: Optional DataLoader for validation data.
        test_loader: Optional DataLoader for test data.
        epochs: Maximum number of training epochs.
        patience: Number of epochs to wait for val loss improvement before stopping.
        device: 'cuda', 'mps', or 'cpu'. Auto-detects if None.
        
    Returns:
        model: The trained model (restored to best validation state if early stopping triggered).
        history: Dictionary containing 'train_loss', 'val_loss', and 'test_loss'.
    """
    if device is None:
        device = torch.device(
            "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
        )
    
    model = model.to(device)
    optimizer = optimizer_class(model.parameters(), lr=lr, weight_decay=weight_decay)
    
    history = {'train_loss': [], 'val_loss': []}
    
    best_val_loss = float('inf')
    best_model_state = None
    epochs_no_improve = 0

    for epoch in range(1, epochs + 1):
        # --- Training Phase ---
        model.train()
        train_loss = 0.0
        for batch_x, batch_y in train_loader:
            batch_x, batch_y = batch_x.to(device), batch_y.to(device)
            
            optimizer.zero_grad()
            outputs = model(batch_x)
            
            # Align shapes if necessary (e.g., 1D vs 2D tensor warnings)
            if outputs.shape != batch_y.shape:
                outputs = outputs.view_as(batch_y)
                
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item() * batch_x.size(0)
            
        train_loss /= len(train_loader.dataset)
        history['train_loss'].append(train_loss)
        
        # --- Validation Phase (Optional) ---
        if val_loader is not None:
            model.eval()
            val_loss = 0.0
            with torch.no_grad():
                for batch_x, batch_y in val_loader:
                    batch_x, batch_y = batch_x.to(device), batch_y.to(device)
                    outputs = model(batch_x)
                    
                    if outputs.shape != batch_y.shape:
                        outputs = outputs.view_as(batch_y)
                        
                    loss = criterion(outputs, batch_y)
                    val_loss += loss.item() * batch_x.size(0)
                    
            val_loss /= len(val_loader.dataset)
            history['val_loss'].append(val_loss)
            
            # --- Early Stopping Check ---
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                best_model_state = copy.deepcopy(model.state_dict())
                epochs_no_improve = 0
            else:
                epochs_no_improve += 1
                
            if patience is not None and epochs_no_improve >= patience:
                print(f"Early stopping triggered at epoch {epoch}. Restoring best weights.")
                model.load_state_dict(best_model_state)
                break

            #if epochs/epoch % 5 == 0: 
            print(f'Epoch: {epoch} - Validation Loss: {val_loss}')

    # If we finish training without triggering early stopping, make sure we return the best model anyway
    if val_loader is not None and best_model_state is not None and epochs_no_improve < patience if patience else True:
        model.load_state_dict(best_model_state)

    # --- Test Phase (Optional) ---
    if test_loader is not None:
        model.eval()
        test_loss = 0.0
        with torch.no_grad():
            for batch_x, batch_y in test_loader:
                batch_x, batch_y = batch_x.to(device), batch_y.to(device)
                outputs = model(batch_x)
                
                if outputs.shape != batch_y.shape:
                    outputs = outputs.view_as(batch_y)
                    
                loss = criterion(outputs, batch_y)
                test_loss += loss.item() * batch_x.size(0)
                
        test_loss /= len(test_loader.dataset)
        history['test_loss'] = test_loss
        print(f"Final Test Loss: {test_loss:.6f}")

    return model, history

class TrajectoryDataset(Dataset):
    def __init__(self, trajectories, window_length=3):
        self.trajectories = torch.as_tensor(trajectories, dtype=torch.float32)
        self.window_length = window_length
        self.Ntrajectories = self.trajectories.shape[0]
        self.Ntimes = self.trajectories.shape[1]
        self.Npieces_per_trajectory = self.Ntimes - self.window_length

    def __len__(self):
        return self.Ntrajectories * self.Npieces_per_trajectory

    def __getitem__(self, index):
        trajectory_index = index // self.Npieces_per_trajectory 
        
        start = index % self.Npieces_per_trajectory 
        stop = start + self.window_length
        
        trajectory = self.trajectories[trajectory_index] 
        
        X = trajectory[start:stop].reshape(-1) 
        Y = trajectory[stop]                   
        
        return X, Y