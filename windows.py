from utils import *

data_gdp, data_population = get_data()
plt.rcParams['font.sans-serif'] = ['SimHei']
window = tk.Tk()
countrylist = data_gdp['GDP, current prices (Billions of U.S. dollars)'][1:229].tolist()  # 国家列表
indexmap = {'GDP': 'gdp', '人口': 'renkou'}
indexlist = list(indexmap)
typemap = {'线形图': 'line', '柱状图': 'bar'}
window.title('经济指标曲线图')
w_width = 1100
w_height = 750
scn_width = window.maxsize()[0]
x_point = (scn_width - w_width) // 2
window.geometry('%dx%d+%d+%d' % (w_width, w_height, x_point, 100))
window.wm_attributes('-topmost', True)
window.tk_focusFollowsMouse()
window.bind("<Escape>", lambda event: window.iconify())
frame0 = tk.Frame(window, pady=10, padx=15)
frame0.grid(row=0, column=0, sticky='w')


# 全选反选
def unselectall():
    for index, item in enumerate(countrylist):
        v[index].set('')


# 全选
def selectall():
    for index, item in enumerate(countrylist):
        v[index].set(item)


frame1 = tk.Frame(window, pady=6, padx=15)
frame1.grid(row=1, column=0)
opt = tk.IntVar()
v = []
for index, item in enumerate(countrylist):
    v.append(tk.StringVar())
    ttk.Checkbutton(frame1, text=item, variable=v[-1], onvalue=item, offvalue="").grid(row=index // 7 + 1,
                                                                                       column=index % 7, sticky='w')
ttk.Radiobutton(frame1, text='全选', variable=opt, value=1, command=selectall).grid(row=0, column=0, sticky='w')
ttk.Radiobutton(frame1, text='反选', variable=opt, value=0, command=unselectall).grid(row=0, column=1, sticky='w')
frame2 = tk.Frame(window, padx=15, pady=15)
frame2.grid(row=2, column=0, sticky='w')
var = tk.StringVar()
type = tk.StringVar()
ttk.Label(frame2, text="请选择指标:").grid(row=0, column=0, sticky='w')
chosen = ttk.Combobox(frame2, textvariable=var)
chosen.grid(row=0, column=1, sticky='w')
chosen['values'] = indexlist
chosen.current(0)

ttk.Label(frame2, text="请选择图表类型:").grid(row=0, column=2, sticky='w')
chosen = ttk.Combobox(frame2, textvariable=type)
chosen.grid(row=0, column=3, sticky='w')
chosen['values'] = ['线形图', '柱状图']
chosen.current(0)  # 默认是第一个

start_year = tk.StringVar()
end_year = tk.StringVar()
start_year.set('1980')
nowyear = datetime.datetime.now().strftime('%Y')
end_year.set(nowyear)
ttk.Label(frame2, text="起始年份").grid(row=0, column=4, sticky='w', pady=6)
ttk.Spinbox(frame2, textvariable=start_year, from_=1980, to=nowyear, increment=1).grid(row=0, column=5, sticky='w')
ttk.Label(frame2, text="结束年份").grid(row=0, column=6, sticky='w')
ttk.Spinbox(frame2, textvariable=end_year, from_=1980, to=nowyear, increment=1).grid(row=0, column=7)
ttk.Button(frame2, text="点击获取曲线图", command=get_plt).grid(row=0, column=8)
window.mainloop()
