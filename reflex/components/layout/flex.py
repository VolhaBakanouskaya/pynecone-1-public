"""A reflexive container component."""

from reflex.components.libs.chakra import ChakraComponent
from reflex.vars import Var


class Flex(ChakraComponent):
    """A reflexive container component."""

    tag = "Flex"

    # How to align items in the flex.
    align: Var[str]

    # Shorthand for flexBasis style prop
    basis: Var[str]

    # Shorthand for flexDirection style prop
    direction: Var[str]

    # Shorthand for flexGrow style prop
    grow: Var[str]

    # The way to justify the items.
    justify: Var[str]

    # Shorthand for flexWrap style prop
    wrap: Var[str]

    # Shorthand for flexShrink style prop
    shrink: Var[str]
