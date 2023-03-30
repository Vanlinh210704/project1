class Nhan_vien:

    def __init__ (self):
        self.info_staff= {}
        self.luong = {}
    
    def input_infor (self):
        self.info_staff['Mã nhân viên'] = int(input('Nhập mã nhân viên của bạn: '))
        self.info_staff['Tên'] = input('Nhập tên của bạn: ')
        self.info_staff['Tuổi'] = int(input('Nhập tuổi của bạn: '))
        self.info_staff['Tiền Lương'] = int(input('Nhập số tiền lương của bạn(Vnd): '))
        self.info_staff['Tổng giờ làm'] = int(input('Nhập tổng thời gian làm của bạn(giờ): '))    
    
    def tinh_thuong(self):
        if self.info_staff['Tổng giờ làm'] >= 200:
            self.info_staff['Lương thưởng'] = self.info_staff['Tiền Lương'] * 0.2
            self.luong['Tổng Tiền lương'] = self.info_staff['Lương thưởng'] + self.info_staff['Tiền Lương']
        elif 100 <= self.info_staff['Tổng giờ làm'] < 200:
            self.info_staff['Lương thưởng'] = self.info_staff['Tiền Lương'] * 0.1
            self.luong['Tổng Tiền lương'] = self.info_staff['Lương thưởng'] + self.info_staff['Tiền Lương']
        else:
            self.info_staff['Lương thưởng'] = 0
            self.luong['Tổng Tiền lương'] = self.info_staff['Lương thưởng'] + self.info_staff['Tiền Lương']
    
    def print_infor (self):
        print('----Thông Tin của bạn----')
        for infor in self.info_staff:
            print(f'{infor} - {self.info_staff[infor]}')
        print('-------------------------')
        for cash in self.luong:
            print(f'{cash} - {self.luong[cash]} (vnd)')
        print('-------------------------')
    

nhan_vien_1 = Nhan_vien()
nhan_vien_1.input_infor()
nhan_vien_1.tinh_thuong()
nhan_vien_1.print_infor()


