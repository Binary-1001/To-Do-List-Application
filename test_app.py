import unittest
from app import *
from unittest.mock import patch


class TestApp(unittest.TestCase):
    @patch("builtins.input",return_value = "code")
    def test_add_task(self,mock_input):
        result = add_task()
        self.assertIn("code",result)
        self.assertEqual(result["code"]["is_it_done"], "❌")

    @patch("builtins.input",return_value = "code")
    def test_mark_as_done_task_found(self,mock_input):
        result = mark_as_done()
        self.assertIn("code",result)
        self.assertNotIn("rap",result)
        self.assertEqual(result["code"]["is_it_done"], "✅")

    @patch("builtins.input", return_value="dance")
    def test_mark_as_done_not_found(self, mock_input):
        tasks.clear()
        tasks["code"] = {"is_it_done": "❌"}

        result = mark_as_done()

        self.assertEqual(result, "Task : dance does not exist\n")
    
    @patch("builtins.input",return_value = "host a workshop")
    def test_delete_task_found(self,mock_input):
        tasks.clear()
        tasks.update({"host a workshop":{"is_it_done":"❌"}})
        tasks.update({
           "Watch a data engineering elective workshop":{"is_it_done":"❌"}
        })

        result = delete_task()

        excepted = {
           "Watch a data engineering elective workshop":{"is_it_done":"❌"}
        }

        self.assertEqual(result,excepted)

    @patch("builtins.input",return_value = "see j.cole")
    def test_delete_task_not_found(self,mock_input):
        tasks.clear()
        tasks.update({"rap":{"is_it_done":"❌"}})
 
        result = delete_task()

        self.assertEqual(result,"Can't delete : see j.cole it does not exists")

    





if __name__ == "__main__":
    unittest.main()