- Link Aplikasi PWS :

- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1.  Membuat sebuah proyek Django baru.
> Saya membuat proyek Django dengan nama dairy-products-ecommerce.
> Lalu, saya membuka terminal dan berpindah ke direktori yang sudah disiapkan untuk proyek.
> Saya menjalankan perintah django-admin startproject dairy_products_ecommerce untuk membuat struktur dasar proyek Django.

2. Membuat aplikasi dengan nama main pada proyek tersebut.
> Saya tetap berada di direktori proyek dan membuat aplikasi baru bernama main menggunakan perintah python manage.py startapp main.
> Django kemudian membuat struktur awal aplikasi, termasuk folder migrations, views.py, models.py, dan lainnya.

3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
> Saya membuka file settings.py pada direktori proyek utama (dairy_products_ecommerce) dan menambahkan 'main' ke dalam daftar INSTALLED_APPS untuk memberitahu Django bahwa aplikasi ini aktif.
> Saya membuka file urls.py pada direktori proyek utama dan menambahkan rute untuk aplikasi main dengan cara path('', include('main.urls')), agar aplikasi ini bisa diakses melalui URL.

4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut. (name, price, description)
> Saya membuka file models.py pada aplikasi main.
> Saya membuat model Product yang memiliki atribut name, price, dan description sesuai dengan kebutuhan. Saya juga menambahkan atribut tambahan seperti fat content, quantity, dan rating.
> Setelah membuat model, saya menjalankan perintah python manage.py makemigrations dan python manage.py migrate untuk membuat dan menerapkan perubahan database.

5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
> Saya membuka file views.py di aplikasi main.
> Saya membuat fungsi show_main yang akan mengembalikan template HTML dengan data seperti nama aplikasi, nama saya, dan kelas saya.
> Di dalam fungsi ini, saya menggunakan render untuk menampilkan template dengan data yang dikirimkan.

6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
> Saya membuat file urls.py di dalam folder aplikasi main jika belum ada.
> Saya menambahkan rute baru dengan path('', views.show_main) untuk menghubungkan URL ke fungsi show_main yang telah dibuat di views.py.

7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
> Setelah semua bagian selesai, saya membuka terminal dan melakukan commit semua perubahan ke Git.
> Saya melakukan deploy aplikasi ke PWSdengan mengikuti prosedur deployment yang sesuai.
> Setelah berhasil deploy, saya menguji aplikasi melalui browser untuk memastikan aplikasi bisa diakses secara online.

- Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Berikut adalah link bagannya : https://drive.google.com/file/d/14ILUORqEUW764DEfm-vm_n9y9uN6xlh7/view?usp=sharing 

- Jelaskan fungsi git dalam pengembangan perangkat lunak!
Fungsi git adalah untuk mengelola versi kode, berkolaborasi antar pengembang, melacak perubahan, dan memperbaiki kesalahan. Git mempermudah pengelolaan proyek secara aman dan terstruktur.

- Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django dipilih sebagai framework permulaan pembelajaran pengembangan perangkat lunak karena kemudahan penggunaannya, fitur built-in yang lengkap, dan struktur yang jelas mengikuti pola Model-View-Template (MVT). Django memungkinkan pemula untuk membangun aplikasi web dengan cepat dan aman sambil memahami konsep arsitektur dan praktik pengembangan yang baik.

- Mengapa model pada Django disebut sebagai ORM?
Model Django disebut ORM (Object-Relational Mapping) karena menghubungkan objek Python dengan tabel di database, memungkinkan pengembang untuk melakukan operasi database (seperti membuat, membaca, memperbarui, dan menghapus data) menggunakan objek Python, tanpa perlu menulis SQL secara langsung.