from pylab import *
mpl.rcParams['font.sans-serif'] = ['Times New Roman']

#labels表示你不同类别的代号，比如这里的demo中有13个类别
labels = ['WHE', 'GH', 'GAR', 'URB', 'FL', 'NCL', 'OTH', 'WAT']
tick_marks = np.array(range(len(labels))) + 0.5

def plot_confusion_matrix(cm, title='Confusion Matrix', cmap=plt.cm.binary):
    # plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.imshow(cm, interpolation='nearest', cmap='Blues')#, vmin=999999999, vmax=1000000000)
    plt.title(title)
    plt.colorbar()
    xlocations = np.array(range(len(labels)))
    plt.xticks(xlocations, labels, rotation=0)
    plt.yticks(xlocations, labels)


cm = np.array([[99.16236461, 43.73799048, 86.71315779, 97.74835354, 82.26776221, 54.78744159, 17.86399666, 30.71840395],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]])


ind_array = np.arange(len(labels))
x, y = np.meshgrid(ind_array, ind_array)
fig, ax = plt.subplots()

for x_val, y_val in zip(x.flatten(), y.flatten()):
    c = cm[y_val][x_val]
    print(x_val)
    print(y_val)
    print('-'*50)
    plt.text(x_val, y_val, "%0.2f" % (c,), color='tomato', fontsize=10, va='center', ha='center', weight='bold') #"%0.2f" % (c,)

# offset the tick
plt.gca().set_xticks(tick_marks, minor=True)
plt.gca().set_yticks(tick_marks, minor=True)
plt.gca().xaxis.set_ticks_position('none')
plt.gca().yaxis.set_ticks_position('none')
plt.grid(True, which='minor', linestyle='-', linewidth=1, color='Black')
ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)
plt.tick_params(bottom=False, top=False, left=False, right=False)
plt.gcf().subplots_adjust(bottom=0.15)

plot_confusion_matrix(cm, title='')
fig.tight_layout()
plt.xlabel('x',fontsize=12)
plt.ylabel('y',fontsize=12)
plt.xlabel('Predicted class Part F in 2019   Part B in 2020    Part E in 2021    Part F in 2021') #Y轴标签
plt.ylabel('Reference class') #Y轴标签
# show confusion matrix
# plt.savefig('../Data/confusion_matrix.png', format='png')
plt.savefig(r'D:\gaofen2222.jpg', dpi=500, bbox_inches='tight')
plt.show()

