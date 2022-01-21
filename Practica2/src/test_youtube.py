'''
Created on 20 ene 2022

@author: MC
'''
from Youtube import lee_trending_videos,parsea_fecha,video_mas_likeability_por_categoria,incrementos_visitas    
#media_visitas_2,video_mayor_ratio_likes_dislikes,media_visitas      

def test_lee_trending_videos(ruta_fichero):
    registro=lee_trending_videos(ruta_fichero)
    print(registro[:3])
    print('Hay {} videos en el dataset'.format(len(registro)))


def test_media_visitas(video,fecha):
    media=media_visitas(video,fecha)
    print(media)
'''
def test_media_visitas_2(video,fecha):
    media=media_visitas_2(video,fecha)
    print(media)
    
def test_video_mayor_ratio_likes_dislikes(video,categoria):
    ratio=video_mayor_ratio_likes_dislikes(video,categoria)
    print(ratio)


'''


if __name__ == '__main__':
    video=test_lee_trending_videos('../data/Youtube.csv')
    fecha=parsea_fecha('1/1/2017')
    #media_visitas(video, fecha)
    #test_media_visitas_2(video,fecha)
    #categoria='Entertainment'
    #test_video_mayor_ratio_likes_dislikes(video,categoria)
    video_mas_likeability_por_categoria(video,k=20)
    incrementos_visitas(video,canal)
    