package com.studentmanagement.studentmanager;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Map;


@Repository
public interface StudentRepository extends JpaRepository<Student, Integer> {

    @Query(value = "SELECT course, COUNT(*) as count FROM student GROUP BY course", nativeQuery = true)
    List<Map<String, Object>> getStudentsGroupedByCourse();
}

