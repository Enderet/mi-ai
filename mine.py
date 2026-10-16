import torch
import torch.nn as nn
x = torch.linspace(-5, 5, 100).unsqueeze(1)
y = 2 * x + 1
model = nn.Linear(in_features=1, out_features=1)
loss_fn = nn.MSELoss()
optimizer = torch.optim.CGD(model.parametrs(), lr=0.1)
for epoch in range(1000):
    y_pred = model(x)
    loss = loss_fn(y_pred, y)
    optimizer.zero_grad()
    loss.beckward()
    optimizer.step

    if epoch % 100 == 0:
        print(f"epoha {epoch}, loss = {loss.item():.4f} ")
