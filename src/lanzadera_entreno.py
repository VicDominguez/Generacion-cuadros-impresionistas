from cyclegan import CycleGAN
from lector_imagenes import LectorImagenes
from utilidades import Utilidades

if __name__ == "__main__":
    utils = Utilidades()
    logger = utils.obtener_logger("lanzadera entrenamiento")

    utils.asegurar_dataset()
    logger.info("Dataset en linea")

    logger.info("Creacion de la red neuronal")
    gan = CycleGAN("resnet")
    logger.info("Red neuronal lista")

    logger.info("Iniciando el lector de imágenes")
    lector = LectorImagenes()
    logger.info("Imágenes listas")

    logger.info("Comienzo del entrenamiento")
    gan.train(lector)

