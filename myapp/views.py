from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .forms import LoginForm
from django.views.generic import View
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to MySQL
            return redirect('success_page')  # Redirect after successful save
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
def toppick(request, id):
    # Sample movie data with more details
    movies = {
        1: {
            'title': 'Green Book',
            'description': ' Green book กรีนบุ๊ค หนังที่อ้างอิงมาจากเรื่องจริงของนักดนตรีผิวสีอย่าง ดอน เชอร์ลีย์ กับคนขับรถของเขาชาวอเมริกันเชื้อสายอิตาเลียนอย่าง โทนี ลิป ที่ย้อนกลับไปในปี 1930-1960 ที่คนผิวสีในอเมริกานั้นต้องพกหนังสือที่ชื่อว่า "The Negro Motorist Green Book" หรือเรียกสั้นๆว่า "Green Book" ที่เป็นเหมือนหนังสือไกด์แนะนำร้านอาหาร โรงแรม หรือสถานที่ที่ต้อนรับคนผิวสีในขณะนั้น เพราะในช่วงเวลานั้นมีการเหยียดผิวที่รุนแรงมากถึงขั้นเสียชีวิตเลยก็มีในการเดินทางไปทั่วอเมริกาเพื่อทำการแสดง แต่ในยุคนั้นมีการเหยียดผิวที่รุนแรงเกือบทั่วอเมริกา',
            'director': 'Peter Farrelly',
            'release_date': '2018-11-16',
            'genre': 'Drama, Comedy',
            'poster': 'POSTER1.png',
            'video': 'green.mp4',
            'img' : 'greenbookactor.jpg',
            'actor_image': 'greenbookactor.jpg',
            'actors': [
                {'name': 'Viggo Mortensen', 'image': 'Viggo Mortensen.JPG'},
                {'name': 'Mahershala Ali', 'image': 'Mahershala Ali.JPG'},
                {'name': 'Linda Cardellini', 'image': 'Linda Cardellini.JPG'},
                {'name': 'Sebastian Maniscalco', 'image': 'linda.jpg'},
                {'name': 'Dimiter D. Marinov', 'image': 'linda.jpg'},
                {'name': 'Joe Cortese', 'image': 'linda.jpg'},
                {'name': 'Irene Sirko', 'image': 'linda.jpg'},
                {'name': 'P.J. Byrne', 'image': 'linda.jpg'},
                {'name': 'Michael McKinney', 'image': 'linda.jpg'},
                {'name': 'Misty Copeland', 'image': 'linda.jpg'},
            ]
        },
        2: {
            'title': 'Black Panther',
            'description': 'เรียกว่าเป็นโปรแกรมหนังซูเปอร์ฮีโรของ Marvel Studios ที่รอคอยมากที่สุดของปีนี้แล้วล่ะครับ สำหรับ ‘Black Panther: Wakanda Forever’ หรือ ‘แบล็ค แพนเธอร์: วาคานด้าจงเจริญ’ ถ้าพูดในเชิงของภาพยนตร์ นี่คือหนังภาคต่อของ ‘Black Panther’ (2018) หนังซูเปอร์ฮีโรที่ครองใจคนทั้งโลกและนักวิจารณ์หลังออกฉาย สร้างรายทั่วโลกถล่มทลายกว่า 1,346 ล้านเหรียญ แถมยังเป็นหนังค่าย Marvel เรื่องแรกที่ได้รับการเสนอชื่อเข้าชิงรางวัลออสการ์สาขาภาพยนตร์ยอดเยี่ยม ก่อนจะคว้ามาได้ถึง 3 รางวัล แต่ถ้าพูดในแง่ของหนังภายใต้จักรวาล MCU (Marvel Cinematic Universe) หนังเรื่องนี้คือหนังปิดจักรวาลเฟส 4 ครับ ตัวหนังภาคนี้ก็เลยมีความน่าสนใจว่า จะเล่าเรื่องและทำหน้าที่ส่งจักรวาลสู่เฟส 5 และ 6 ที่จะเกิดขึ้นในอนาคตในทิศทางใด',
            'director': 'Ryan Coogler',
            'release_date': '2018-02-16',
            'genre': 'Action, Adventure',
            'poster': 'POSTER2.png',  # Fallback image if video is unavailable
            'video': 'blackpanter.mp4',  # Background video for Black Panther
            'actor_image': 'blackpantheractor.jpg',  # Fallback actor image
            'actors': [
                {'name': 'Chadwick Boseman', 'image': 'Viggo.jpeg'},
                {'name': 'Michael B. Jordan', 'image': 'mahershala.jpg'},
                {'name': 'Lupita Nyong', 'image': 'linda.jpg'},
                {'name': 'Danai Gurira', 'image': 'linda.jpg'},
                {'name': 'Martin Freeman', 'image': 'linda.jpg'},
                {'name': 'Daniel Kaluuya', 'image': 'linda.jpg'},
                {'name': 'Letitia Wright', 'image': 'linda.jpg'},
                {'name': 'Winston Duke', 'image': 'linda.jpg'},
                {'name': 'Sterling K. Brown', 'image': 'linda.jpg'},
                {'name': 'Angela Bassett', 'image': 'linda.jpg'},
            ]
        },
        3: {
            'title': 'Moonfall',
            'description': 'ไบรอัน ฮาร์เปอร์ (นำแสดงโดย แพทริก วิลสัน Patrick Wilson) อดีตนักบินอวกาศที่เคยบาดหมางกับนาซาจำต้องกลับมาร่วมภารกิจครั้งใหม่กับ โจซินดา ฟาวล์ (นำแสดงโดย ฮัลลี เบอร์รี Halle Berry) อดีตเพื่อนร่วมงานของเขาอีกครั้งหลังจากเคซี เฮาส์แมน (นำแสดงโดยจอห์น แบรดลีย์ John Bradley) หนุ่มเนิร์ดที่ค้นพบว่าดวงจันทร์เปลี่ยนเส้นทางโคจรและกำลังจะพุ่งชนโลกนำความวิบัติมาสู่ทุกชีวิต ชะตากรรมของโลกจึงอยู่ในมือของพวกเขา',
            'director': 'Roland Emmerich',
            'release_date': '2022-02-04',
            'genre': 'Science Fiction, Action',
            'poster': 'POSTER3.png',
            'video': 'moonfall.mp4',
            'actor_image': 'moonfallactor.jpg',
            'actors': [
                {'name': 'Halle Berry', 'image': 'halle.jpg'},
                {'name': 'Patrick Wilson', 'image': 'patrick.jpg'},
                {'name': 'John Bradley', 'image': 'john.jpg'},
                {'name': 'Donald Sutherland', 'image': 'john.jpg'},
                {'name': 'Michael Peña', 'image': 'john.jpg'},
                {'name': 'Charlie Plummer', 'image': 'john.jpg'},
                {'name': 'Kelly Yu', 'image': 'john.jpg'},
                {'name': 'Max Mauff', 'image': 'john.jpg'},
                {'name': 'Elyes Gabel', 'image': 'john.jpg'},
                {'name': 'Catherine Keener', 'image': 'john.jpg'},
            ]
        },
        4: {
            'title': 'Titanic',
            'description': 'เป็นภาพยนตร์มหากาพย์โรแมนติก-ภัยพิบัติที่ออกฉายในปี 1997 กำกับโดย James Cameron และเขียนบทโดย Cameron และ Rose DeWitt Bukater ภาพยนตร์เรื่องนี้ติดตาม Rose DeWitt Bukater (รับบทโดย Kate Winslet) หญิงสาวชนชั้นสูงที่ไม่พอใจกับชีวิตที่ถูกกำหนดไว้ และ Jack Dawson (รับบทโดย Leonardo DiCaprio) ช่างวาดรูปหนุ่มผู้ยากไร้ พวกเขาตกหลุมรักกันบนเรือ RMS Titanic ในระหว่างการเดินทางครั้งแรกของเรือ',
            'director': 'James Cameron',
            'release_date': '1997-12-19',
            'genre': 'Drama, Romance',
            'poster': 'POSTER4.png',
            'video': 'titanic.mp4',
            'actor_image': 'titanicactor.jpg',
            'actors': [
                {'name': 'Leonardo DiCaprio', 'image': 'leo.jpg'},
                {'name': 'Kate Winslet', 'image': 'kate.jpg'},
                {'name': 'Billy Zane', 'image': 'billy.jpg'},
                {'name': 'Kathy Bates', 'image': ''},
                {'name': 'Frances Fisher', 'image': ''},
                {'name': 'Gloria Stuart', 'image': ''},
                {'name': 'Bill Paxton', 'image': ''},
                {'name': 'Bernard Hill', 'image': ''},
                {'name': 'David Warner', 'image': ''},
                {'name': 'Victor Garber', 'image': ''},
            ]
        },
        5: {
            'title': 'Friday the 13th',
            'description': 'เรื่องราวของกลุ่มวัยรุ่นที่ถูกล่าโดยฆาตกรสวมหน้ากากในวันศุกร์ที่ 13',
            'director': 'Sean S. Cunningham',
            'release_date': '1980-05-09',
            'genre': 'Horror, Thriller',
            'poster': 'POSTER5.png',
            'video': '13friday.mp4',
            'actor_image': 'fridayactor.jpg',
            'actors': [
                {'name': 'Betsy Palmer', 'image': 'betsy.jpg'},
                {'name': 'Adrienne King', 'image': 'adrienne.jpg'},
                {'name': 'Jeannine Taylor', 'image': 'harry.jpg'},
                {'name': 'Robbi Morgan', 'image': 'harry.jpg'},
                {'name': 'Kevin Bacon', 'image': 'harry.jpg'},
                {'name': 'Harry Crosby', 'image': 'harry.jpg'},
                {'name': 'Laurie Bartram', 'image': 'harry.jpg'},
                {'name': 'Mark Nelson', 'image': 'harry.jpg'},
                {'name': 'Renee Jones ', 'image': 'harry.jpg'},
                {'name': 'Peter Browning', 'image': 'harry.jpg'},
            ]
        },
        6: {
            'title': '9Sadtra',
            'description': 'หนังแนวไซไฟที่เล่าเรื่องการสำรวจอวกาศที่ห่างไกล',
            'director': 'Jane Doe',
            'release_date': '2023-08-15',
            'genre': 'Science Fiction, Drama',
            'poster': 'POSTER6.png',
            'video': '99.mp4',
            'actor_image': 'sadtraactor.jpg',
            'actors': [
                {'name': 'Actor P', 'image': 'actorP.jpg'},
                {'name': 'Actor Q', 'image': 'actorQ.jpg'},
                {'name': 'Actor R', 'image': 'actorR.jpg'},
            ]
        },
    }

    # Get the selected movie by ID, with a default fallback
    movie = movies.get(id, {
        'title': 'Unknown Movie',
        'description': 'No description available',
        'poster': 'default.png',
        'actor_image': 'defaultactor.jpg',
        'actors': []
    })

    # Here you would typically render a template with the movie data
    # Example: return render(request, 'movie_detail.html', {'movie': movie})
    return render(request, 'toppick.html', {'movie': movie})



def coming_soon_detail(request, id):
    # ดึงข้อมูลหนังที่กำลังจะมาในอนาคต
    movie = {'id': id, 'title': f'Coming Soon {id}', 'description': 'ตัวอย่างหนัง'}
    return render(request, 'coming_soon_detail.html', {'movie': movie})

def celebrity_detail(request, id):
    # ดึงข้อมูลดารา
    celebrity = {'id': id, 'name': f'Celebrity {id}', 'bio': 'ข้อมูลของดารา'}
    return render(request, 'celebrity_detail.html', {'celebrity': celebrity})

def news_detail(request, id):
    # ดึงข้อมูลข่าว
    news = {'id': id, 'title': f'News {id}', 'content': 'เนื้อหาข่าว'}
    return render(request, 'news_detail.html', {'news': news})

def search_movies(request):
    query = request.GET.get('q', '').strip()
    movies = {
        1: {'title': 'Green Book'},
        2: {'title': 'Black Panther'},
        3: {'title': 'Moonfall'},
        4: {'title': 'Titanic'},
        5: {'title': 'Friday the 13th'},
        6: {'title': '9Sadtra'},
    }
    
    # Search for the movie
    for id, movie in movies.items():
        if movie['title'].lower() == query.lower():
            return redirect(reverse('toppick', args=[id]))

    # If no match, show a "not found" page or similar
    return HttpResponse("Movie not found", status=404)