from __future__ import annotations

import uvicorn

from backend.Logs.logger import JsonLogger
from backend.Memory.memory_manager import MemoryManager
from backend.MobileAPI.app import create_app
from backend.TrainingPipeline.recorder import TrainingRecorder
from backend.core.config import load_settings
from backend.orchestrator import Orchestrator


def main() -> None:
    settings = load_settings()
    logger = JsonLogger(log_dir=settings.log_dir, level=settings.log_level)
    trainer = TrainingRecorder(data_dir=settings.data_dir)
    memory = MemoryManager(data_dir=settings.data_dir)
    orchestrator = Orchestrator(memory=memory, logger=logger, trainer=trainer)

    app = create_app(orchestrator, required_token=settings.api_token)

    uvicorn.run(app, host=settings.api_host, port=settings.api_port, log_level=settings.log_level.lower())


if __name__ == "__main__":
    main()
