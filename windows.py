from utils import *


class Windows:
    def __init__(self):
        self.data_gdp, self.data_population = get_data()
        self.countrylist = self.data_gdp['GDP, current prices (Billions of U.S. dollars)'][1:229].tolist()  # 国家列表
        self.indexmap = {'GDP': 'gdp', '人口': 'renkou'}
        self.indexlist = list(self.indexmap)
        self.window = None
        self.v = []
        self.var = None
        self.start_year = None
        self.end_year = None

    def build_windows(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        self.window = tk.Tk()
        self.window.title('经济指标曲线图')
        w_width = 1100
        w_height = 750
        scn_width = self.window.maxsize()[0]
        x_point = (scn_width - w_width) // 2
        self.window.geometry('%dx%d+%d+%d' % (w_width, w_height, x_point, 100))
        self.window.tk_focusFollowsMouse()
        self.window.bind("<Escape>", lambda event: self.window.iconify())
        frame0 = tk.Frame(self.window, pady=10, padx=15)
        frame0.grid(row=0, column=0, sticky='w')
        frame1 = tk.Frame(self.window, pady=6, padx=15)
        frame1.grid(row=1, column=0)
        opt = tk.IntVar()
        for index, item in enumerate(self.countrylist):
            self.v.append(tk.StringVar())
            ttk.Checkbutton(frame1, text=item, variable=self.v[-1], onvalue=item, offvalue="").grid(row=index // 7 + 1,
                                                                                                    column=index % 7,
                                                                                                    sticky='w')
        ttk.Radiobutton(frame1, text='全选', variable=opt, value=1, command=self.selectall).grid(row=0, column=0,
                                                                                                 sticky='w')
        ttk.Radiobutton(frame1, text='反选', variable=opt, value=0, command=self.unselectall).grid(row=0, column=1,
                                                                                                   sticky='w')
        frame2 = tk.Frame(self.window, padx=15, pady=15)
        frame2.grid(row=2, column=0, sticky='w')
        self.var = tk.StringVar()
        ttk.Label(frame2, text="请选择指标:").grid(row=0, column=0, sticky='w')
        chosen = ttk.Combobox(frame2, textvariable=self.var)
        chosen.grid(row=0, column=1, sticky='w')
        chosen['values'] = self.indexlist
        chosen.current(0)
        self.start_year = tk.StringVar()
        self.end_year = tk.StringVar()
        self.start_year.set('1980')
        nowyear = datetime.datetime.now().strftime('%Y')
        self.end_year.set(nowyear)
        ttk.Label(frame2, text="起始年份").grid(row=0, column=4, sticky='w', pady=6)
        ttk.Spinbox(frame2, textvariable=self.start_year, from_=1980, to=nowyear, increment=1).grid(row=0, column=5,
                                                                                                    sticky='w')
        ttk.Label(frame2, text="结束年份").grid(row=0, column=6, sticky='w')
        ttk.Spinbox(frame2, textvariable=self.end_year, from_=1980, to=nowyear, increment=1).grid(row=0, column=7)
        ttk.Button(frame2, text="点击获取曲线图", command=self.get_plt).grid(row=0, column=8)

    def unselectall(self):
        for index, item in enumerate(self.countrylist):
            self.v[index].set('')

    def selectall(self):
        for index, item in enumerate(self.countrylist):
            self.v[index].set(item)

    def get_plt(self):
        index = self.var.get()  # 经济指标
        if index == 'GDP':
            data = self.data_gdp
            name = 'GDP, current prices (Billions of U.S. dollars)'
        elif index == '人口':
            data = self.data_population
            name = 'Population (Millions of people)'
        chosed = [i.get() for i in self.v if i.get()]
        startyear = self.start_year.get()
        if not startyear:
            messagebox.showerror('警告', '没有起始年份')
            return False
        endyear = self.end_year.get()
        if not endyear:
            messagebox.showerror('警告', '没有结束年份')
            return False
        endyear = str(int(endyear) + 1)
        year_label = [i for i in range(int(startyear), int(endyear))]
        for country in chosed:
            start_index = int(startyear) - 1980
            end_index = int(endyear) - 1980
            data_x = np.array(data.loc[data[name] == country].iloc[:, start_index + 1:end_index + 1]).flatten()
            # print(data_x)
            plt.plot(year_label, data_x, label=country)
            plt.xlabel("year")
            plt.ylabel(index)
            plt.legend(loc="best")
        plt.show()

    def start(self):
        self.window.mainloop()
