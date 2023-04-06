from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

def pdf_func(scale, point, xs, target_prob):
    # Adjust scale so probability at point is target_prob
    target_prob = norm(loc=0, scale=1).pdf(1)/max(norm(loc=0, scale=1).pdf(xs)) # prob at 1 std dev
    value = (norm(loc=0, scale=scale).pdf([point])/max(norm(loc=0, scale=scale).pdf(xs)))-target_prob
    return value

fig, ax = plt.subplots(1, 1)

for action_duration in [2, 6, 10, 15]:
    # action_duration = 10  # s
    act_time = action_duration/2  # start/stop point each side of mean, s.
    x = np.linspace(-(2), (2*action_duration+2), 1000)

    mean = action_duration
    # std = 1
    # rv = norm(loc=mean, scale=std)
    # ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
    # ax.plot(x, rv.pdf(x)/max(rv.pdf(x)), 'k-', lw=2, label='frozen pdf')

    target_prob = None
    opt_scale = fsolve(pdf_func, 1, args=(act_time, x, target_prob)) # find std dev value, initial guess 1
    target_prob = norm(loc=0, scale=opt_scale).pdf(opt_scale)/max(norm(loc=0, scale=opt_scale).pdf(x))
    print(opt_scale)
    # print(pdf_func(opt_scale, act_time, x, target_prob))  # should be zero
    rv = norm(loc=mean, scale=opt_scale)
    ax.plot(x, rv.pdf(x)/max(rv.pdf(x)), 'b-', lw=2, label='frozen pdf')
    ax.plot([act_time, act_time, act_time+action_duration, act_time+action_duration], [0, target_prob, target_prob, 0], 'r-')

    start_time = mean-(2*opt_scale)
    stop_time = mean+(2*opt_scale)
    ax.plot([start_time, start_time], [0, 1], 'g-')
    ax.plot([stop_time, stop_time], [0, 1], 'g-')

plt.show()
