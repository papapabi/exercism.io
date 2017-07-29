class Grains
  class << self
    BOARD_TOTAL = 18_446_744_073_709_551_615
   
    # Finds the amount of grains of wheat in the nth chessboard square given
    # that the number on each successive square doubles.
    def square(n)
      raise ArgumentError.new('N should be in closed interval [1, 64]') unless (1..64).include? n
      list, e = [], self.grains
      list << e.next until list.size == n
      list.last
    end

    # Returns the total number of grains on the board. 
    def total
      BOARD_TOTAL
    end

    # Returns an enumerator for the ruleset: 'number of grains of wheat on a
    # chessboard given that the number on each square doubles.'
    def grains
      grains = Enumerator.new do |y|
        result = 1
        loop do
          y << result
          result *= 2
        end
      end
    end
  end
end

module BookKeeping
  VERSION = 1
end
