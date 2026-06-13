import cv2
import dlib
from imutils import face_utils

# Inicializar el detector de rostros y la función para extraer características faciales
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("ruta_correcta/shape_predictor_68_face_landmarks.dat")

def capture_and_process():
    # Inicializar la cámara
    cap = cv2.VideoCapture(0)

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

            # Extraer las características faciales
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            for (x, y) in shape:
                cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

        # Mostrar el cuadro con los rostros detectados
        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_process()
