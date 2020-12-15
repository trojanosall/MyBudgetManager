import hashlib

import MyBudgetManager.MyBudgetManager.Log.logs as logs


def md5sum(path, blocksize=65536):
    """Create hash from a given file.

    Parameters
    ----------
    path : string
        the path of the file
    blocksize : int, optional
        [description] (the default is 65536, which [default_description])

    Returns
    -------
    string
        the hashed code of the file
    """

    logs.logger.debug("Create hash from a given file.")
    try:
        hash = hashlib.md5()
        with open(path, "rb") as file:
            for block in iter(lambda: file.read(blocksize), b""):
                hash.update(block)
        return hash.hexdigest()
    except Exception as e:
        logs.logger.error(e, exc_info=True)
