class Anagram
  attr_reader :chars, :s

  def initialize(s)
    @s = s
    @chars = s.downcase.split("").sort
  end

  def match(a)
    a.reject { |e| e.length != s.length }
      .reject { |e| e.downcase == s.downcase }.select do |e|
      e.downcase.split("").sort == @chars
    end
  end
end

module BookKeeping
  VERSION = 2
end
