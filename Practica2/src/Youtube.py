'''
Created on 18 ene 2022

@author: MC
'''
import csv
from collections import namedtuple
from datetime import datetime,date

registro=namedtuple('registro','idd,fecha_trending,titulo,canal,categoria,visitas,likes,dislikes')

def lee_trending_videos(ruta_fichero):
    with open (ruta_fichero, encoding='utf-8') as f:
        lector=csv.reader(f, delimiter=';')
        next(lector)
        video=[]
        for idd,fecha_trending,titulo,canal,categoria,visitas,likes,dislikes in lector:
            fecha_trending=parsea_fecha(fecha_trending)
            visitas=int(visitas)
            likes=int(likes)
            dislikes=int(dislikes)
            tupla=registro(idd,fecha_trending,titulo,canal,categoria,visitas,likes,dislikes)
            video.append(tupla)
    return video

def parsea_fecha(fecha):
    return datetime.strptime(fecha,'%d/%m/%Y').date()
'''
def media_visitas(video,fecha):
    try:
        j=sum(x.visitas for x in video if x.fecha_trending==fecha)/len([x.visitas for x in video if x.fecha_trending==fecha])
        return j
        
    except ZeroDivisionError:
        j=0
        return j

def video_mayor_ratio_likes_dislikes(video,categoria=None):
    if categoria !=None:  
        k=max(((video,x.likes/x.dislikes) for x in video if x.categoria==categoria and x.dislikes!=0), key=lambda n:n[1])[0]
        k=set('No existe tal categoria en este dataset' for x in video if x.categoria !=categoria )
    else:
        k=max(((video,x.likes/x.dislikes) for x in video if x.dislikes!=0), key=lambda n:n[1])[0]

    return k
    
    
def video_mayor_ratio_likes_dislikes_2(video,categoria=None):
    pass
    '''

def media_visitas_2(video,fecha):
    k=[x.visitas for x in video if x.fecha_trending==fecha]
    l=sum(k)
    if k != 0:
        media=l/len(k)
    else:
        media=0
    return media

def canales_top(video,n=3):
    top=dict()
    for x in video:
        if x.canal not in top:
            top[x]=1
        else:
            top[x]+=1
    top1=top.items()
    top1.sort(top1,key=lambda n:n[1])
    return top1[:n]

def video_mas_likeability_por_categoria(video,k=20):
    like=dict()
    for x in video:
        if x.categoria in like:
                like[x].append(video)
        else:
            like[x]=[video]
            
    for l in like:
        m=like[l]
        b=max((aux2(j,k)for j in m),key=lambda n:n[1])
        like[l]=b[0]
    return like

def aux2(j,k):
    k=(j.id,(k*j.likes-j.dislikes)/(k*j.visitas))
    return k

    
    
def aux1(j,p):
    i=j-p 
    return i

def incrementos_visitas(video,canal):
    k=[x.visitas for x in video if x.canal==canal]
    l=k[1:]
    v=[aux1(j,p) for j,p in zip(l,k)]
    return v


    
    