"""
Le but principal de ce challenge est de s'exercer sur le module tqdm
"""

from tqdm import tqdm
from pytube import YouTube

SAVE_PATH = "C:\\Users\\***\\Downloads"

# lien de la vidéo à télécharger
lien = "https://www.youtube.com/watch?v=xWOoBJUqlbI"


def video_objet(lien):
    """
    Crée un objet YouTube pour une URL donnée et filtre les fichiers vidéo disponibles.

    Parameters
    ----------
    lien : str
        URL de la vidéo YouTube à télécharger.

    Returns
    -------
    tuple
        Un tuple contenant le nom du fichier et l'objet vidéo correspondant.

    Notes
    -----
    Cette fonction utilise la bibliothèque pytube pour créer un objet YouTube à partir de l'URL spécifiée.
    Ensuite, elle filtre les fichiers vidéo disponibles pour ne sélectionner que ceux avec l'extension "mp4".
    Elle renvoie le nom du fichier (défini manuellement) et l'objet vidéo correspondant.

    Examples
    --------
    >>> video_objet("https://www.youtube.com/watch?v=xWOoBJUqlbI")
    ('GeeksforGeeks Video', <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F"
    acodec="mp4a.40.2" progressive="True" type="video">)
    """

    try:
        yt = YouTube(lien)
    except:
        print("Erreur de connexion")

    mp4files = yt.streams.filter(file_extension='mp4')

    nom_fichier = 'GeeksforGeeks Video'

    video = yt.streams.get_by_itag(mp4files[-1].itag)
    return nom_fichier, video


def telecharge(nom_fichier, video):
    """
    Télécharge une vidéo à partir de son objet YouTube.

    Parameters
    ----------
    nom_fichier : str
        Nom du fichier de la vidéo à télécharger.
    video : pytube.Stream
        Objet vidéo à télécharger.

    Returns
    -------
    None

    Notes
    -----
    Cette fonction utilise l'objet vidéo passé en paramètre pour télécharger la vidéo à partir de l'URL spécifiée.
    Elle utilise tqdm pour afficher la progression du téléchargement en temps réel.

    Examples
    --------
    >>> telecharge("GeeksforGeeks Video", video)
    """

    try:
        print("Je télécharge")
        with tqdm(total=video.filesize, unit='bytes', unit_scale=True) as pbar:
            video.download(SAVE_PATH, filename=nom_fichier,
                           filename_prefix='Downloading: ',
                           progress_callback=lambda stream, chunk, bytes_remaining: pbar.update(chunk))
    except:
        print("Une erreur est survenue lors du téléchargement!")
    print('Tâche terminée!')


nom_fichier, video = video_objet(lien)
telecharge(nom_fichier=nom_fichier, video=video)
