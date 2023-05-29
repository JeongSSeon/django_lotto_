from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

# Create your views here.

# 유저의 http 요청을 request 파라미터가 받아옴
def index(request):
    
    # request.POST -> dict
    # - dict의 key == input tag의 name 값
    # - dict의 value == input tag의 value 값 (== USER의 입력값)

    # request.POST['fname'] -> '안녕하세요'
    # request.POST['lname'] -> '반갑습니다.'

    lottos = GuessNumbers.objects.all # 전체 행 꺼내기

    return render(request, 'lotto/default.html', {'lottos':lottos}) #context dict


def post(request):


    if request.method == 'POST': # POST 요청이 들어온 경우

        form = PostForm(request.POST)

        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate()

            return redirect('index')

    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})


    return HttpResponse("<h1>Hello, world!</h1>")

def hello(request):

    # data = GuessNumbers.objects.all()  # == from GuessNumbers select *
    # data = GuessNumbers.objects.get(id=1) # == from GuessNumbers select id

    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")


def detail(request, lottokey):

    lotto = GuessNumbers.objects.get(id=lottokey)
    
    return render(request, 'lotto/detail.html', {'lotto':lotto})





    # index.html
    # <input name='name' type='text'></input> # 입력창 - 유저가 웹에서 입력 네임 -> win the prize 입력 가정
    # <input name='text' type='text'></input> # 입력창 - 유저가 웹에서 입력한 텍스트
    # USER가 값을 입력하고, 전송 버튼을 클릭 -> USER가 입력한 값을 가지고 HTTP POST request

    # user_input_name = request.POST['name'] # HTML에서 name이 'name'인 input tag에 대해 USER가 입력한 값 꺼냄
    # user_input_text = request.POST['text'] # HTML에서 name이 'text'인 input tag에 대해 USER가 입력한 값 꺼내는 코드

    # new_row = GuessNumbers(name=user_input_name, text=user_input_text) # guessnumbers 테이블에 하나의 행 만들기. 따로 입력 안 한 열은 디폹트

    # print(new_row.num_lotto)  # 5  하나의 행에 있는 열의 값 수정 및 처리 가능
    # print(new_row.name)  # 'win the prize!'

    # new_row.name = new_row.name.upper()  # WIN THE PRIZE! 
    # new_row.lottos = [np.randint(1,50) for i in range(6)]

    # new_row.save() # == 커밋 (행.save())

    # return HttpResponse('<h1>Hello, world!</h1>')


        # 1. models.py에서 함수 정의했을 때..
        # new_row.generate()


# 2. models.py에서 함수 정의 안 하고 views.py에서 직접 실행시킬 수 있음 / 이 때는 1번 지워
        # new_row.lottos = ""
        # origin = list(range(1,46)) # 1~45의 숫자 리스트 [1, 2, 3, ..., 43, 44, 45]
        # # 6개 번호 set 갯수만큼 1~46 뒤섞은 후 앞의 6개 골라내어 sorting
        # for _ in range(0, new_row.num_lotto): # 총 5번 돌아.. 디폴트 5니까
        #     random.shuffle(origin) # [10, 21, 36, 2, ... , 1, 11]
        #     guess = origin[:6] # [10, 21, 36, 2, 15, 23]
        #     guess.sort() # [2, 10, 15, 21, 23, 36]
        #     new_row.lottos += str(guess) +'\n' # 로또 번호 str에 6개 번호 set 추가 -> '[2, 10, 15, 21, 23, 36]\n'
        #     # -> new_row.lottos : '[2, 10, 15, 21, 23, 36]\n[1, 15, 21, 27, 30, 41]\n...'
        # new_row.update_date = timezone.now()
        # new_row.save() # GuessNumbers object를 DB에 저장 / self: 클래스 객체변수 하나 -> new_row
