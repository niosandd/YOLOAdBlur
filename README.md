# Подготовка датасета для обучения

1. Запускаем making_frames_for_dataset.py
 - На вход video_path подаем путь к видео
 - output_dir

2. Находим скрипт adding_white_space_to_img.ipynb
 - Запускаем Jupyter и заходим в папку notebooks.
 - input_folder -> путь к датасету, который получился от making_frames_for_dataset.py
 - output_folder -> на выход папка с белыми изображениями 

3. Находим скрипт change_image_size_on_all_folders.ipynb
 - image_folder -> путь к датасету, который получился от adding_white_space_to_img.ipynb
 - output_folder -> на выход папка с белыми изображениями 

4. Запуск скрипта test.ipynb
 - image_folder -> путь к датасету, который получился от change_image_size_on_all_folders.ipynb
 - pattern_folder -> путь к датасету, в котором хранятся паттерны
 - output_folder -> финальный датасет с картинками для обучения


# Обучение

1. yolo.py
 - Закомментировал часть кода под train
 - Закомментировал часть кода под predict