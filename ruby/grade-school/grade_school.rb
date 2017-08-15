class School
  attr_reader :constituents

  def initialize()
    @constituents = []
  end

  def add(student, grade)
    new_student = { grade: grade, students: [student] }
    if target = find_by_grade(grade)
      target[:students] << student
      # Maybe make a custom array that automatically sorts itself?
      target[:students].sort!
    else
      constituents << new_student
    end
  end

  def students(grade)
    target = find_by_grade(grade)
    target.nil? ? [] : target[:students]
  end

  def students_by_grade
    constituents.sort { |a, b| a[:grade] <=> b[:grade] }
  end

  private 
  def find_by_grade(grade) 
    constituents.detect { |e| e.has_value?(grade) }
  end
end

module BookKeeping
  VERSION = 3
end
