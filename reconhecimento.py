from deepface import DeepFace
import os

class Reconhecimento:
    def __init__(self, db_path="Rostos_cadastrados"):
        self.db_path = db_path
        if not os.path.exists(self.db_path):
            os.makedirs(self.db_path)
            print(f"Pasta '{self.db_path}' criada para armazenar imagens de rostos.")

    def reconhecer(self, imagem_path):
        """
        Tenta reconhecer um rosto em uma imagem (frame).
        """
        try:
           
            resultados = DeepFace.find(
                img_path=imagem_path, 
                db_path=self.db_path,
                model_name="Facenet",
                detector_backend="retinaface",
                enforce_detection=False,
                silent=True
            )
            
           
            if len(resultados) > 0 and not resultados[0].empty:
               
                identity_path = resultados[0]['identity'][0]
                
                
                nome_arquivo = os.path.basename(identity_path)
                nome_usuario = os.path.splitext(nome_arquivo)[0]
                return nome_usuario
            else:
                return "Desconhecido"
                
        except Exception as e:
            print(f"Erro no reconhecimento facial: {e}")
            return "Desconhecido"


        