class Clock
  attr_reader :hours, :minutes

  def initialize(hours, minutes)
    @minutes = minutes % 60
    @hours = (hours + minutes / 60) % 24
  end

  def self.at(hours, minutes)
    new(hours, minutes)
  end

  def to_s
    format('%02d:%02d', hours, minutes)
  end

  def +(mins)
    self.class.new(hours, minutes + mins)
  end

  def -(mins)
    self.class.new(@hours, @minutes - mins)
  end

  def ==(other_clock)
    hours == other_clock.hours && minutes == other_clock.minutes
  end
end

module BookKeeping
  VERSION = 2
end
