import torch 
import torch.nn as nn
import torch.optim as optim

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
    def __init__(self, dim, hidden=None, layers=0, bias=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.dim = dim
        self.hidden = hidden if hidden is not None else dim
        self.is_fitted = False
        
        self.net = nn.ModuleList()
        
        if layers == 0:
            self.net.append(nn.Linear(self.dim, self.dim, bias=bias))
        else:
            self.net.append(nn.Linear(self.dim, self.hidden, bias=bias))
            
            for _ in range(layers - 1):
                self.net.append(nn.Linear(self.hidden, self.hidden, bias=bias))
                
            self.net.append(nn.Linear(self.hidden, self.dim, bias=bias))

    def forward(self, x):
        x = x.view(-1, self.dim)
        for layer in self.net:
            x = layer(x)
            
        if self.dim == 1:
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