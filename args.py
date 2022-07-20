from imports import *

@dataclass
class TrainingArgs():

    seed: int = 1
    lr: float = 3e-4
    batch_size: int = 32
    num_workers: int = os.cpu_count()
    max_epochs: str = 200
    device: torch.device = torch.device("cuda" if torch.cuda.is_available() else "cpu") # torch.device("mps" if torch.backends.mps.is_available() else "cpu")

    input_size: int = 3
    output_size: int = 10
    image_size: int = 32
    channels: tuple = (16, 16, 16, 16, 16)
    weights: torch.Tensor = None
    architecture: str = 'DNN'

    data: tuple = None

    root_dir: str = './data/cifar-10'
    checkpoint: str = './checkpoints'
    experiment: str = None

args = TrainingArgs()