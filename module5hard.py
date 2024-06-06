from __future__ import annotations


class UrTube:
    def __init__(self) -> None:
        self.users: list[User] = []
        self.videos: list[Video] = []
        self.current_user: User | None = None

    def log_in(self, login: str, password: str) -> None:
        for user in self.users:
            if user.nickname == login and user.password == hash(password):
                self.current_user = user
                return

    def register(self, nick: str, password: str, age: int) -> None:
        for user in self.users:
            if user.nickname == nick:
                print(f"Пользователь {nick} уже существует")
                return
        self.current_user = User(nick, password, age)
        self.users.append(self.current_user)

    def log_out(self) -> None:
        self.current_user = None

    def add(self, *videos: Video) -> None:
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)

    def get_videos(self, word: str) -> list[Video]:
        return [video for video in self.videos if word.lower() in video.title.lower()]

    def watch_video(self, name: str):
        v = None
        for video in self.videos:
            if video.title.lower() == name.lower():
                v = video
        if not v:
            print("Такого видео не существует")
            return
        if self.current_user:
            if v.adult_mode and self.current_user.age < 18:
                print("Вам нет 18, пожалуйста покиньте страницу")
                return
            for i in range(1, v.duration + 1):
                print(i, end=" ")
            print("Конец видео")
            return
        print("Войдите в аккаунт чтобы смотреть видео")


class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False) -> None:
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self) -> str:
        return f"{self.title}"


class User:
    def __init__(self, nick: str, password: str, age: int) -> None:
        self.nickname, self.password, self.age = nick, hash(password), age

    def __str__(self) -> str:
        return f"Пользователь: {self.nickname} Возраст: {self.age}"

    def __repr__(self):
        return f"{self.nickname} {self.age}"


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
