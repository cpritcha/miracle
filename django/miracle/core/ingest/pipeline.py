import os
import shutil

from .unarchiver import extract
from .analyzer import group_files
from .grouper import group_metadata
from .loader import load_project
from . import ProjectDirectoryAlreadyExists


def run(project, archive, delete_archive_on_failure):
    try:
        project_file_paths = extract(project, archive)
        project_grouped_file_paths = group_files(project_file_paths)
        metadata_project = group_metadata(project_grouped_file_paths)
        load_project(metadata_project)
    except ProjectDirectoryAlreadyExists:
        if delete_archive_on_failure:
            if os.path.exists(archive):
                os.unlink(archive)
        raise
    except Exception:
        cleanup_on_error(project, archive, delete_archive_on_failure)
        raise


def cleanup_on_error(project, archive_path, delete_archive_on_failure):
    project_path = project.project_path
    packrat_path = project.packrat_path

    if delete_archive_on_failure:
        if os.path.exists(archive_path):
            os.unlink(archive_path)
    if os.path.exists(project_path):
        shutil.rmtree(project_path)
    if os.path.exists(packrat_path):
        shutil.rmtree(packrat_path)