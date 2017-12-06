require_relative 'bowling_error'

class Frame
  attr_reader :first, :second
  attr_reader :roll_tracker
  attr_reader :number
  attr_accessor :wait

  def initialize(number)
    @number = number
    @first = @second = @roll_tracker = 0
  end

  def add(pins_knocked_down)
    if roll_tracker == 0
      @first = pins_knocked_down
    elsif roll_tracker == 1
      @second = pins_knocked_down
    else 
      raise BowlingError 
    end
    @roll_tracker += 1
  end

  def tally(n)
    if n == 1
      first
    elsif n == 2
      first + second
    else
      raise BowlingError
    end
  end

  def tenth?
    number == 10
  end

  def strike?
    first == 10
  end

  def spare?
    first + second == 10
  end

  def open?
    first + second < 10
  end

  def total
    first + second
  end

  def to_s
    [number, first, second, bonus, score]
  end

  def finished?
    strike? || roll_tracker > 1
  end

  def rolls
    roll_tracker
  end

  def wait
    @wait ||= if strike?
                2
              elsif spare?
                1
              else 
                0
              end
  end
end 
