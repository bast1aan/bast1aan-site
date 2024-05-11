from typing import Self

from dataclasses import dataclass


@dataclass
class Tag:
	value: str
	
	def __gt__(self, other: Self) -> bool:
		return self.value > other.value


tags: list[Tag] = []
