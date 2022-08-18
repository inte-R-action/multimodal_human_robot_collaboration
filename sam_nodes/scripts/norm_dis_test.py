from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

def pdf_func(scale, point, xs, target_prob):
    target_prob = norm(loc=0, scale=scale).pdf(scale)/max(norm(loc=0, scale=scale).pdf(xs))
    value = (norm(loc=0, scale=scale).pdf([point])/max(norm(loc=0, scale=scale).pdf(xs)))-target_prob
    return value

action_duration = 10  # s
act_time = action_duration/2  # s
x = np.linspace(-(action_duration), (action_duration), 1000)

fig, ax = plt.subplots(1, 1)

mean = 0
std = 1
rv = norm(loc=mean, scale=std)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
ax.plot(x, rv.pdf(x)/max(rv.pdf(x)), 'k-', lw=2, label='frozen pdf')

target_prob = 0.2
opt_scale = fsolve(pdf_func, 1, args=(act_time, x, target_prob))
target_prob = norm(loc=0, scale=opt_scale).pdf(opt_scale)/max(norm(loc=0, scale=opt_scale).pdf(x))
print(opt_scale)
print(pdf_func(opt_scale, act_time, x, target_prob))
std = opt_scale
rv = norm(loc=mean, scale=std)
ax.plot(x, rv.pdf(x)/max(rv.pdf(x)), 'b-', lw=2, label='frozen pdf')

ax.plot([-act_time, -act_time, act_time, act_time], [0, target_prob, target_prob, 0], 'r-')

startstop_time = 2*opt_scale
ax.plot([-startstop_time, -startstop_time], [0, 1], 'g-')
ax.plot([startstop_time, startstop_time], [0, 1], 'g-')

plt.show()
