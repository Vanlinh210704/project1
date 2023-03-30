class Store:
    
    def __init__(self):
        self.menu = {}
        self.cart = []

    def input_menu(self):
        self.so_luong_hang_hoa = int(input('Nhập số lượng hàng hóa: '))
        for i in range(self.so_luong_hang_hoa):
            self.ten_hang_hoa = input('Nhập tên hàng hóa: ')
            self.gia_ban = int(input(f'Nhập giá bán của {self.ten_hang_hoa}: '))
            self.menu[self.ten_hang_hoa] = self.gia_ban

    def print_menu(self):
        print('------MENU------')
        for hang_hoa in self.menu:
            print(f'{hang_hoa} - {self.menu[hang_hoa]}')
        print('----------------')

    def shopping (self):
        while True:
            choice = input('(Gõ "q" nếu bạn không mua)\nBạn muốn mua gì: ')
            check = 0
            if choice == 'q':
                check = 1
                print('Xin cảm ơn')
                break
            for ten in self.menu:
                if choice == ten:
                    so_luong = int(input('Bạn mua bao nhiêu: '))
                    print(f'-Đã thêm {so_luong} {ten} vào giỏ hàng')
                    thanh_tien = (self.menu[ten]) * so_luong
                    self.cart.append(ten)
                    self.cart.append(so_luong)
                    self.cart.append(thanh_tien)
                    check = 1
            if check == 0:
                print('-Không có trong menu thử nhập lại nhé :>')
                
    def print_bill(self):
        tong = 0
        print('---Hóa Đơn---')
        for i in range(0,len(self.cart),3):
            print(f'{self.cart[i]}   x   {self.cart[i+1]}  =  {self.cart[i+2]} vnd')
            tong += self.cart[i+2]
        print(f'-------------\nBạn cần Thanh Toán: {tong} vnd')
        print('Xin chân thành cảm ơnn')

nguoi_mua_1 = Store()
nguoi_mua_1.input_menu()
nguoi_mua_1.print_menu()
nguoi_mua_1.shopping()
nguoi_mua_1.print_bill()