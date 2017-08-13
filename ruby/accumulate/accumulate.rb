module Enumerable
  def accumulate(&block)
    accumulator = []
    self.each do |e|
      accumulator << block.call(e)
    end
    accumulator
  end
end

module BookKeeping
  VERSION = 1
end

