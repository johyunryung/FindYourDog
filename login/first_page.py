import tkinter

class first_page: #첫 화면
  def __init__(self):
      ##기본 창 설정
      CANVAS_SIZE = 1200  # 창의 크기
      self.TILE_SIZE = CANVAS_SIZE / 2

      ##창 생성
      self.root = tkinter.Tk()  # 창
      self.root.geometry(str(CANVAS_SIZE) + 'x' + str(CANVAS_SIZE))  # 속성값을 문자열로 보냄
      self.root.title('Find Your Dog')  # 창의 이름을 바꿔주는 것
      self.root.resizable(width=False, height=False)  # 사이즈를 바꿀 수 있는지 묻는 중
      self.canvas = tkinter.Canvas(self.root, bg='white', width=CANVAS_SIZE, height=CANVAS_SIZE)  # 창, 넓이, 길이등 설정
      self.canvas.pack()  # 다른 요소가 없으면 이대로 실행

      ##이미지 생성
      self.images = {}
      self.images['logo'] = tkinter.PhotoImage(file='logo.gif')  # 이미지 생성

      ##버튼 생성
      b1 = tkinter.Button(self.root, text = "로그인")
      b1.place(x=300, y=400, anchor = 'nw')

  def play(self):
     self.canvas.create_image(400, 180, anchor = 'nw',image = self.images['logo'])
     self.root.mainloop() #윈도우 창을 실행하게 해 줌


if __name__ == '__main__':
    p1 = first_page()
    p1.play()