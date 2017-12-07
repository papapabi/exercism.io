class SpaceAge
  EARTH_YEAR = 31_557_600.0
  attr_reader :seconds
  private_constant :EARTH_YEAR

  def initialize(s)
    @seconds = s
  end

  def on_earth
    to_years
  end

  def on_mercury
    to_years(0.2408467)
  end

  def on_venus
    to_years(0.61519726)
  end

  def on_mars
    to_years(1.8808158)
  end

  def on_jupiter
    to_years(11.862615)
  end

  def on_saturn
    to_years(29.447498)
  end

  def on_uranus
    to_years(84.016846)
  end

  def on_neptune
    to_years(164.79132)
  end

  private

  def to_years(orbital_ratio = 1)
    seconds / (EARTH_YEAR * orbital_ratio)
  end
end

module BookKeeping
  VERSION = 1
end
