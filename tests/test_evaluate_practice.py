"""Kiểm tra tiến trình chấm kế thừa bản vá alias NumPy."""

from evaluate_practice import run_trackeval


def test_run_trackeval_patches_numpy_in_child(tmp_path):
    """Script TrackEval giả nhận alias NumPy và tham số video luyện."""
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    (scripts / "run_mot_challenge.py").write_text(
        "import numpy as np\n"
        "import sys\n"
        "assert np.float is float\n"
        "assert np.int is int\n"
        "assert '--BENCHMARK' in sys.argv\n"
        "assert 'LAB21' in sys.argv\n"
        "assert 'video_1' in sys.argv\n"
    )

    run_trackeval(tmp_path, "lan_thu", "LAB21", "train")
