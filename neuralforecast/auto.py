# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/models.ipynb.

# %% auto 0
__all__ = ['AutoRNN', 'AutoLSTM', 'AutoGRU', 'AutoTCN', 'AutoDilatedRNN', 'AutoMLP', 'AutoNBEATS', 'AutoNHITS']

# %% ../nbs/models.ipynb 2
from os import cpu_count
import torch

from ray import tune
from ray.tune.search.basic_variant import BasicVariantGenerator

from .common._base_auto import BaseAuto

from .models.rnn import RNN
from .models.gru import GRU
from .models.tcn import TCN
from .models.lstm import LSTM
from .models.dilated_rnn import DilatedRNN

from .models.mlp import MLP
from .models.nbeats import NBEATS
from .models.nhits import NHITS

from .losses.pytorch import MAE
from .losses.pytorch import MSE

# %% ../nbs/models.ipynb 8
class AutoRNN(BaseAuto):
    
    default_config = {
        "input_size_multiplier": [-1, 4, 16, 64],
        "h": None,
        "encoder_hidden_size": tune.choice([50, 100, 200, 300]),
        "encoder_n_layers": tune.randint(1, 4),
        "context_size": tune.choice([5, 10, 50]),
        "decoder_hidden_size": tune.choice([64, 128, 256, 512]),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "max_steps": tune.choice([500, 1000]),
        "batch_size": tune.choice([16, 32]),
        "loss": tune.choice([MAE(), MSE()]),
        "random_seed": tune.randint(1, 20)
    }

    def __init__(self,
                 h,
                 config=None, 
                 search_alg=BasicVariantGenerator(random_state=1),
                 num_samples=10,
                 refit_with_val=False,
                 cpus=cpu_count(),
                 gpus=torch.cuda.device_count(),
                 verbose=False):
        """ Auto RNN
        
        **Parameters:**<br>
        
        """
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()        
            config['input_size'] = tune.choice([h*x \
                         for x in self.default_config["input_size_multiplier"]])
            del config["input_size_multiplier"]

        super(AutoRNN, self).__init__(
              cls_model=RNN, 
              h=h,
              config=config, 
              search_alg=search_alg,
              num_samples=num_samples, 
              refit_with_val=refit_with_val,
              cpus=cpus,
              gpus=gpus,
              verbose=verbose
        )

# %% ../nbs/models.ipynb 13
class AutoLSTM(BaseAuto):

    default_config = {
        "input_size_multiplier": [-1, 4, 16, 64],
        "h": None,
        "encoder_hidden_size": tune.choice([50, 100, 200, 300]),
        "encoder_n_layers": tune.randint(1, 4),
        "context_size": tune.choice([5, 10, 50]),
        "decoder_hidden_size": tune.choice([64, 128, 256, 512]),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "max_steps": tune.choice([500, 1000]),
        "batch_size": tune.choice([16, 32]),
        "loss": tune.choice([MAE(), MSE()]),
        "random_seed": tune.randint(1, 20)
    }

    def __init__(self,
                 h,
                 config, 
                 search_alg=BasicVariantGenerator(random_state=1),
                 num_samples=10,
                 refit_with_val=False,
                 cpus=cpu_count(),
                 gpus=torch.cuda.device_count(),
                 verbose=False):

        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()        
            config['input_size'] = tune.choice([h*x \
                         for x in self.default_config["input_size_multiplier"]])
            del config["input_size_multiplier"]

        super(AutoLSTM, self).__init__(
              cls_model=LSTM,
              h=h,
              config=config,
              search_alg=search_alg,
              num_samples=num_samples,
              refit_with_val=refit_with_val,
              cpus=cpus,
              gpus=gpus,
              verbose=verbose
        )

# %% ../nbs/models.ipynb 17
class AutoGRU(BaseAuto):

    default_config = {
        "input_size_multiplier": [-1, 4, 16, 64],
        "h": None,
        "encoder_hidden_size": tune.choice([50, 100, 200, 300]),
        "encoder_n_layers": tune.randint(1, 4),
        "context_size": tune.choice([5, 10, 50]),
        "decoder_hidden_size": tune.choice([64, 128, 256, 512]),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "max_steps": tune.choice([500, 1000]),
        "batch_size": tune.choice([16, 32]),
        "loss": tune.choice([MAE(), MSE()]),
        "random_seed": tune.randint(1, 20)
    }

    def __init__(self,
                 h,
                 config,
                 search_alg=BasicVariantGenerator(random_state=1),
                 num_samples=10,
                 refit_with_val=False,
                 cpus=cpu_count(),
                 gpus=torch.cuda.device_count(),
                 verbose=False):
        
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()        
            config['input_size'] = tune.choice([h*x \
                         for x in self.default_config["input_size_multiplier"]])
            del config["input_size_multiplier"]

        super(AutoGRU, self).__init__(
              cls_model=GRU,
              h=h,
              config=config, 
              search_alg=search_alg,
              num_samples=num_samples,
              refit_with_val=refit_with_val,
              cpus=cpus,
              gpus=gpus,
              verbose=verbose
        )

# %% ../nbs/models.ipynb 21
class AutoTCN(BaseAuto):

    default_config = {
        "input_size_multiplier": [-1, 4, 16, 64],
        "h": None,
        "encoder_hidden_size": tune.choice([50, 100, 200, 300]),
        "context_size": tune.choice([5, 10, 50]),
        "decoder_hidden_size": tune.choice([64, 128]),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "max_steps": tune.choice([500, 1000]),
        "batch_size": tune.choice([16, 32]),
        "loss": tune.choice([MAE()]),
        "random_seed": tune.randint(1, 20)
    }

    def __init__(self,
                 h,
                 config,
                 search_alg=BasicVariantGenerator(random_state=1),
                 num_samples=10,
                 refit_with_val=False,
                 cpus=cpu_count(),
                 gpus=torch.cuda.device_count(),
                 verbose=False):
        
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()        
            config['input_size'] = tune.choice([h*x \
                         for x in self.default_config["input_size_multiplier"]])
            del config["input_size_multiplier"]

        super(AutoTCN, self).__init__(
              cls_model=TCN,
              h=h,
              config=config, 
              search_alg=search_alg,
              num_samples=num_samples,
              refit_with_val=refit_with_val,
              cpus=cpus,
              gpus=gpus,
              verbose=verbose
        )

# %% ../nbs/models.ipynb 25
class AutoDilatedRNN(BaseAuto):

    default_config = {
        "input_size_multiplier": [-1, 4, 16, 64],
        "h": None,
        "cell_type": tune.choice(['LSTM', 'GRU']),
        "encoder_hidden_size": tune.choice([50, 100, 200, 300]),
        "dilations": tune.choice([ [[1, 2], [4, 8]], [[1, 2, 4, 8]] ]),
        "context_size": tune.choice([5, 10, 50]),
        "decoder_hidden_size": tune.choice([64, 128, 256, 512]),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "max_steps": tune.choice([500, 1000]),
        "batch_size": tune.choice([16, 32]),
        "loss": tune.choice([MAE(), MSE()]),
        "random_seed": tune.randint(1, 20)
    }

    def __init__(self,
                 h,
                 config, 
                 search_alg=BasicVariantGenerator(random_state=1),
                 num_samples=10,
                 refit_with_val=False,
                 cpus=cpu_count(),
                 gpus=torch.cuda.device_count(),
                 verbose=False):
        
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()        
            config['input_size'] = tune.choice([h*x \
                         for x in self.default_config["input_size_multiplier"]])
            del config["input_size_multiplier"]

        super(AutoDilatedRNN, self).__init__(
              cls_model=DilatedRNN,
              h=h,
              config=config,
              search_alg=search_alg,
              num_samples=num_samples, 
              refit_with_val=refit_with_val,
              cpus=cpus,
              gpus=gpus,
              verbose=verbose
         )

# %% ../nbs/models.ipynb 30
class AutoMLP(BaseAuto):

    default_config = {
        "input_size_multiplier": [1, 2, 3, 4, 5],
        "h": None,
        "hidden_size": tune.choice( [256, 512, 1024] ),
        "num_layers": tune.randint(2, 6),
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "normalize": tune.choice([True, False]),
        "max_steps": tune.choice([500, 1000]),
        "batch_size": tune.choice([32, 64, 128, 256]),
        "windows_batch_size": tune.choice([128, 256, 512, 1024]),
        "loss": tune.choice([MAE(), MSE()]),
        "random_seed": tune.randint(1, 20),
    }

    def __init__(self,
                 h,                 
                 config, 
                 search_alg=BasicVariantGenerator(random_state=1),
                 num_samples=10,
                 refit_with_val=False,
                 cpus=cpu_count(),
                 gpus=torch.cuda.device_count(),
                 verbose=False):

        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()        
            config['input_size'] = tune.choice([h*x \
                         for x in self.default_config["input_size_multiplier"]])

            # Rolling windows with step_size=1 or step_size=h
            # See `BaseWindows` and `BaseRNN`'s create_windows
            config['step_size'] = tune.choice([1, h])
            del config["input_size_multiplier"]

        super(AutoMLP, self).__init__(
              cls_model=MLP,
              h=h,
              config=config, 
              search_alg=search_alg,
              num_samples=num_samples, 
              refit_with_val=refit_with_val,
              cpus=cpus,
              gpus=gpus,
              verbose=verbose
        )

# %% ../nbs/models.ipynb 34
class AutoNBEATS(BaseAuto):

    default_config = {
        "input_size_multiplier": [1, 2, 3, 4, 5],
        "h": None,
        "learning_rate": tune.loguniform(1e-4, 1e-1),
        "normalize": tune.choice([True, False]),
        "max_steps": tune.choice([500, 1000]),
        "batch_size": tune.choice([32, 64, 128, 256]),
        "windows_batch_size": tune.choice([128, 256, 512, 1024]),
        "loss": tune.choice([MAE(), MSE()]),
        "random_seed": tune.randint(1, 20),
    }

    def __init__(self,
                 h,
                 config=None, 
                 search_alg=BasicVariantGenerator(random_state=1),
                 num_samples=10,
                 refit_with_val=False,
                 cpus=cpu_count(),
                 gpus=torch.cuda.device_count(),
                 verbose=False):
        
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()        
            config['input_size'] = tune.choice([h*x \
                         for x in self.default_config["input_size_multiplier"]])

            # Rolling windows with step_size=1 or step_size=h
            # See `BaseWindows` and `BaseRNN`'s create_windows
            config['step_size'] = tune.choice([1, h])
            del config["input_size_multiplier"]

        super(AutoNBEATS, self).__init__(
              cls_model=NBEATS, 
              h=h,
              config=config,
              search_alg=search_alg,
              num_samples=num_samples, 
              refit_with_val=refit_with_val,
              cpus=cpus,
              gpus=gpus,
              verbose=verbose
        )

# %% ../nbs/models.ipynb 38
class AutoNHITS(BaseAuto):

    default_config = {
       "input_size_multiplier": [1, 2, 3, 4, 5],
       "h": None,
       "n_pool_kernel_size": tune.choice([3*[1], 3*[2], 3*[4], 
                                          [8, 4, 1], [16, 8, 1]]),
       "n_freq_downsample": tune.choice([[168, 24, 1], [24, 12, 1], 
                                         [180, 60, 1], [60, 8, 1], 
                                         [40, 20, 1], [1, 1, 1]]),
       "learning_rate": tune.loguniform(1e-4, 1e-1),
       "normalize": tune.choice([True, False]),
       "max_steps": tune.choice([500, 1000]),
       "batch_size": tune.choice([32, 64, 128, 256]),
       "windows_batch_size": tune.choice([128, 256, 512, 1024]),
       "loss": tune.choice([MAE(), MSE()]),
       "random_seed": tune.randint(1, 20),
    }

    def __init__(self,
                 h,
                 config=None, 
                 search_alg=BasicVariantGenerator(random_state=1),
                 num_samples=10,
                 refit_with_val=False,
                 cpus=cpu_count(),
                 gpus=torch.cuda.device_count(),
                 verbose=False):
        
        # Define search space, input/output sizes
        if config is None:
            config = self.default_config.copy()        
            config['input_size'] = tune.choice([h*x \
                         for x in self.default_config["input_size_multiplier"]])
            
            # Rolling windows with step_size=1 or step_size=h
            # See `BaseWindows` and `BaseRNN`'s create_windows
            config['step_size'] = tune.choice([1, h])
            del config["input_size_multiplier"]

        super(AutoNHITS, self).__init__(
              cls_model=NHITS, 
              h=h,
              config=config,
              search_alg=search_alg,
              num_samples=num_samples,
              refit_with_val=refit_with_val,
              cpus=cpus,
              gpus=gpus,
              verbose=verbose
        )
