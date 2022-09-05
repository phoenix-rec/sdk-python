from abc import abstractmethod
from typing import Optional


class Options(object):
    def __init__(self):
        self.request_id: Optional[str] = None


class Option(object):
    @abstractmethod
    def fill(self, options: Options) -> None:
        raise NotImplementedError

    @staticmethod
    def conv_to_options(opts: tuple) -> Options:
        options: Options = Options()
        for opt in opts:
            opt.fill(options)
        return options

    @staticmethod
    def with_request_id(request_id: str):
        class OptionImpl(Option):
            def fill(self, options: Options) -> None:
                options.request_id = request_id

        return OptionImpl()
