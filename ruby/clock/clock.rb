class Clock
  attr_reader :hours, :minutes

  def initialize(hours, minutes)
    @minutes = roll_over_minutes(minutes)
    @hours = roll_over_hours(hours)
  end

  def self.at(hours, minutes)
    new(hours, minutes)
  end

  def to_s
    format('%02d:%02d', hours, minutes)
  end

  def +(clock)
  end

  def roll_over_minutes(minutes)
    @hours = (minutes/60).floor
    minutes % 60
  end

  def roll_over_hours(hours)
    (@hours + hours) % 24
  end

  private :roll_over_minutes, :roll_over_hours
end
