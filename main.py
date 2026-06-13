# main.py                                                                                                             
                                                                                                                      
import cv2                                                                                                            
import dlib                                                                                                           
from imutils import face_utils                                                                                        
                                                                                                                      
def capture_and_process():                                                                                            
    # Inicializar la cámara                                                                                           
    cap = cv2.VideoCapture(0)                                                                                         
                                                                                                                      
    # Cargar el detector de rostros pre-entrenado de Dlib                                                             
    detector = dlib.get_frontal_face_detector()                                                                       
                                                                                                                      
    while True:                                                                                                       
        ret, frame = cap.read()                                                                                       
        if not ret:                                                                                                   
            break                                                                                                     
                                                                                                                      
        # Convertir la imagen a escala de grises para mejorar la detección del rostro                                 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                                                                
                                                                                                                      
        # Detectar los rostros en el cuadro actual                                                                    
        rects = detector(gray, 0)                                                                                     
                                                                                                                      
        for rect in rects:                                                                                            
            (x, y, w, h) = face_utils.rect_to_bb(rect)                                                                
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)                                              
                                                                                                                      
        # Mostrar el cuadro con los rostros detectados                                                                
        cv2.imshow("Frame", frame)                                                                                    
                                                                                                                      
        if cv2.waitKey(1) & 0xFF == ord('q'):                                                                         
            break                                                                                                     
                                                                                                                      
    cap.release()                                                                                                     
    cv2.destroyAllWindows()                                                                                           
                                                                                                                      
if __name__ == "__main__":                                                                                            
    capture_and_process()      