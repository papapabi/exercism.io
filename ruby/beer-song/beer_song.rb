class BeerSong
  def initialize
  end

  def verse(n)
    first(n) + "\n" + second(n) + "\n"
  end

  def verses(s, e)
    s.downto(e).map { |n| verse(n) }.join("\n")
  end


  private
  ZERO_FIRST = "No more bottles of beer on the wall, no more bottles of beer."
  ZERO_SECOND= "Go to the store and buy some more, 99 bottles of beer on the wall."
  private_constant :ZERO_FIRST, :ZERO_SECOND

  def first(n)
    return ZERO_FIRST if n == 0
    b = bottle_plurality(n) 
    "#{n} #{b} of beer on the wall, #{n} #{b} of beer."
  end

  def second(n)
    return ZERO_SECOND if n == 0
    b = bottle_plurality(n - 1)
    p = (n == 1) ? "it" : "one"
    n = (n == 1) ? "no more" : n - 1
    "Take #{p} down and pass it around, #{n} #{b} of beer on the wall."
  end

  def bottle_plurality(n)
    (n == 1) ? "bottle" : "bottles"
  end
end

module BookKeeping
  VERSION = 3
end
