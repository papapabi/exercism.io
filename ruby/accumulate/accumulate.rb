module Enumerable
  def accumulate()
    if block_given?
      [].tap { |accumulator| each { |e| accumulator << yield(e) } }
    else
      enum_for(:accumulate) { size } unless block_given?
    end
  end
end

module BookKeeping
  VERSION = 1
end

