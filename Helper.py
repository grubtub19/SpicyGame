class Helper:

    # This can neither modify class state nor object state.
    @staticmethod
    def loadSprite(filename):
        """Assumes that there is no trailing newline at the end
        end of the .txt file."""
        with open(filename) as f:
            sprite = []
            for line in f:
                sprite.append(line.rstrip())
        return sprite
