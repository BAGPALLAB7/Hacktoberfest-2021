import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

aapl = pd.read_csv('aapl.csv')
print(aapl.head())

# Initialize the short and long windows
short_window = 40
long_window = 100

#Initialize the 'signals' DataFrame with the 'signal' column
signals = pd.DataFrame(index=aapl.index)
signals['signal'] = 0.0

# Create short simple moving average over the short window
signals['short_mavg'] = aapl['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

# Create long simple moving average over the long window
signals['long_mavg'] = aapl['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create Signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)

# Generate trading orders
signals['positions'] = signals['signal'].diff()

print(signals)


### Static Plot using Matplotlib

fig = plt.figure()

# Add subplot and label for y-axis
ax1 = fig.add_subplot(111, ylabel='Price is $')

# Plot the closing price
aapl['Close'].plot(ax=ax1, color='r', lw=2.)

# Plot the short and long moving averages
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

# Plot the buy signals
ax1.plot(signals.loc[signals.positions == 1.0].index, signals.short_mavg[signals.positions == 1.0], 
        '^', markersize=10, color='g')

# Plot the sell signals
ax1.plot(signals.loc[signals.positions == -1.0].index, signals.short_mavg[signals.positions == -1.0], 
        'v', markersize=10, color='k')

plt.show()


### Interactive Plot using Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=aapl.index, y=aapl['Close'], mode='lines', name='lines'))
fig.add_trace(go.Scatter(x=signals.index, y = signals['short_mavg'], mode='lines', name=str(short_window)))
fig.add_trace(go.Scatter(x=signals.index, y = signals['long_mavg'], mode='lines', name=str(long_window)))
fig.add_trace(go.Scatter(mode = 'markers', x = signals.loc[signals.positions == 1.0].index, y = signals.short_mavg[signals.positions == 1.0], 
                        name='Buy', 
                        marker_symbol = 'triangle-up',
                        marker = dict(color='green', size=10)
                        ))
fig.add_trace(go.Scatter(mode = 'markers', x = signals.loc[signals.positions == -1.0].index, y = signals.short_mavg[signals.positions == -1.0], 
                        name='Sell',
                        marker_symbol='triangle-down',
                        marker = dict(color='red', size=10)
                        ))

fig.show()