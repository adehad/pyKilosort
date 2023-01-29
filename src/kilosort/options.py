"""All KiloSort options."""
from __future__ import annotations

import math

import pydantic


class Options(pydantic.BaseModel):
    """Config options for Kilosort."""

    nt0: int = 60
    """Number of time samples for the templates
    (has to be <=81 due to GPU shared memory)"""

    nt0min: int = int(math.ceil(20 * nt0 / 61))
    """time sample where the negative peak should be aligned.
    If -1, comp"""

    ntbuff: int
    """TODO"""

    NT: int
    """number of timepoints per batch"""

    NchanTOT: int
    """total number of channels in the raw binary file, including dead, auxiliary etc"""

    nfilt_factor: int = 4
    """Something on setting upper bound on # of templates"""

    fbinary: str
    """filepath"""

    fs: int
    """Sampling Rate (Hz)"""

    chanMap: str
    """Channel Map"""

    @pydantic.validator("nt0min")
    def peak_alignment_within_template(cls, value):
        """Validate nt0min."""
        if value > cls.nt0:
            raise ValueError(
                "Cannot have negative peak alignment greater than template!"
            )

    @pydantic.validator("NchanTOT")
    def sensible_default_NchanTOT(cls, value):
        """Validate NchanTOT."""
        if value is None:
            value = cls.loadChanMap()  # TODO:
        return value

    @property
    def file_size_bytes(self) -> int:
        """Size in bytes of raw binary."""
        return 0
        # return get_file_size(self.fbinary) # TODO

    @property
    def nTimepoints(self) -> int:
        """Total number of timepoints."""
        return math.floor(self.file_size_bytes / self.NchanTOT / 2)

    @property
    def tstart(self) -> int:
        """Starting timepoint for processing data segment."""
        return 0
        # return math.ceil(self.trange(1) * self.fs) # TODO

    @property
    def tend(self) -> int:
        """Ending timepoint."""
        return 0
        # return min(self.nTimepoints, math.ceil(self.trange(2) * self.fs)) # TODO

    @property
    def sampsToRead(self) -> int:
        """Total number of samples to read."""
        return self.tend - self.tstart

    @property
    def twind(self) -> int:
        """Skip this many bytes at the start."""
        return self.tstart * self.NchanTOT * 2

    @property
    def Nbatch(self) -> int:
        """Number of data batches."""
        return math.ceil(self.sampsToRead / self.NT)

    def loadChanMap(self):
        """Load the Channel Map."""
        # [chanMap, xc, yc, kcoords, NchanTOTdefault]
        pass
        # return loadChanMap(self.chanMap) # TODO

    @property
    def NTbuff(self):
        """Number of timepoints per batch with a buffer applied."""
        return self.NT + 3 * self.ntbuff

    @property
    def Nchan(self):
        """Total number of good channels that we will spike sort."""
        return self.loadChanMap()  # TODO


if __name__ == "__main__":
    # a = Options()
    # a.nt0
    pass
