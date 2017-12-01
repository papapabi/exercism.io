require_relative 'bowling_error'

class Frame
  attr_reader :first, :second, :bonus
  attr_reader :roll_tracker
  attr_reader :number
  attr_accessor :wait

  def initialize(number)
    @number = number
    @first = @second = @bonus = @roll_tracker = 0
  end

  # As of now, Frame#add is highly coupled with the notion of the special 10th frame.
  def add(pins_knocked_down)
    if roll_tracker == 0
      @first = pins_knocked_down
    elsif roll_tracker == 1
      @second = pins_knocked_down
    elsif roll_tracker == 2
      @bonus = pins_knocked_down
    else 
      raise BowlingError 'more than 12 rolls have been thrown'
    end
    @roll_tracker += 1
  end

  def tally(n)
    if n == 1
      first
    elsif n == 2
      first + second
    else
      return BowlingError
    end
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
    first + second + bonus
  end

  def to_s
    [number, first, second, bonus, score]
  end

  def finished?
    if number == 10
      !spare? || roll_tracker > 2
    else 
      strike? || roll_tracker > 1
    end
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
