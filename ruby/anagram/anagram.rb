class Anagram
  attr_reader :chars, :s

  def initialize(s)
    @s = s
    @chars = s.downcase.chars.sort
  end

  def match(a)
    a.reject { |e| e.length != s.length }
      .reject { |e| e.downcase == s.downcase }
      .select { |e| e.downcase.chars.sort == @chars }
  end
end

module BookKeeping
  VERSION = 2
end
