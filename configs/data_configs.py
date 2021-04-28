from configs import transforms_config
from configs.paths_config import dataset_paths


DATASETS = {
	'face2comics': {
		'transforms': transforms_config.SketchToImageTransforms,
		'train_source_root': dataset_paths['train_source'],
		'train_target_root': dataset_paths['train_target'],
		'test_source_root': dataset_paths['test_source'],
		'test_target_root': dataset_paths['test_target'],
	},
}
