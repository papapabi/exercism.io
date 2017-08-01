class Bob
  RESPONSES = { yelling: "Whoa, chill out!",
                question: "Sure.",
                silence: "Fine. Be that way!",
                default: "Whatever." }

  def self.hey(remark)
    normalized_remark = normalize(remark)
    if normalized_remark.empty?
      RESPONSES[:silence]
    elsif yelling?(normalized_remark)
      RESPONSES[:yelling]
    elsif normalized_remark.end_with?("?")
      RESPONSES[:question]
    else
      RESPONSES[:default]
    end
  end

  private

  def self.normalize(remark)
    remark.gsub(/\s+/, ' ').strip
  end

  def self.yelling?(remark)
    remark.upcase == remark && remark.downcase != remark
  end
end

module BookKeeping
  VERSION = 1
end
