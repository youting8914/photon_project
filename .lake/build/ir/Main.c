// Lean compiler output
// Module: Main
// Imports: Init PhotonProject
#include <lean/lean.h>
#if defined(__clang__)
#pragma clang diagnostic ignored "-Wunused-parameter"
#pragma clang diagnostic ignored "-Wunused-label"
#elif defined(__GNUC__) && !defined(__CLANG__)
#pragma GCC diagnostic ignored "-Wunused-parameter"
#pragma GCC diagnostic ignored "-Wunused-label"
#pragma GCC diagnostic ignored "-Wunused-but-set-variable"
#endif
#ifdef __cplusplus
extern "C" {
#endif
LEAN_EXPORT lean_object* _lean_main(lean_object*);
extern lean_object* l_PhotonProject_Basic_hello;
static lean_object* l_main___closed__3;
lean_object* lean_string_push(lean_object*, uint32_t);
static lean_object* l_main___closed__1;
static lean_object* l_main___closed__4;
lean_object* l_IO_print___at_IO_println___spec__1(lean_object*, lean_object*);
LEAN_EXPORT lean_object* l_IO_println___at_main___spec__1(lean_object*, lean_object*);
static lean_object* l_main___closed__2;
lean_object* lean_string_append(lean_object*, lean_object*);
LEAN_EXPORT lean_object* l_IO_println___at_main___spec__1(lean_object* x_1, lean_object* x_2) {
_start:
{
uint32_t x_3; lean_object* x_4; lean_object* x_5; 
x_3 = 10;
x_4 = lean_string_push(x_1, x_3);
x_5 = l_IO_print___at_IO_println___spec__1(x_4, x_2);
return x_5;
}
}
static lean_object* _init_l_main___closed__1() {
_start:
{
lean_object* x_1; 
x_1 = lean_mk_string_unchecked("Hello, ", 7, 7);
return x_1;
}
}
static lean_object* _init_l_main___closed__2() {
_start:
{
lean_object* x_1; lean_object* x_2; lean_object* x_3; 
x_1 = l_main___closed__1;
x_2 = l_PhotonProject_Basic_hello;
x_3 = lean_string_append(x_1, x_2);
return x_3;
}
}
static lean_object* _init_l_main___closed__3() {
_start:
{
lean_object* x_1; 
x_1 = lean_mk_string_unchecked("!", 1, 1);
return x_1;
}
}
static lean_object* _init_l_main___closed__4() {
_start:
{
lean_object* x_1; lean_object* x_2; lean_object* x_3; 
x_1 = l_main___closed__2;
x_2 = l_main___closed__3;
x_3 = lean_string_append(x_1, x_2);
return x_3;
}
}
LEAN_EXPORT lean_object* _lean_main(lean_object* x_1) {
_start:
{
lean_object* x_2; lean_object* x_3; 
x_2 = l_main___closed__4;
x_3 = l_IO_println___at_main___spec__1(x_2, x_1);
return x_3;
}
}
lean_object* initialize_Init(uint8_t builtin, lean_object*);
lean_object* initialize_PhotonProject(uint8_t builtin, lean_object*);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_Main(uint8_t builtin, lean_object* w) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin, lean_io_mk_world());
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_PhotonProject(builtin, lean_io_mk_world());
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
l_main___closed__1 = _init_l_main___closed__1();
lean_mark_persistent(l_main___closed__1);
l_main___closed__2 = _init_l_main___closed__2();
lean_mark_persistent(l_main___closed__2);
l_main___closed__3 = _init_l_main___closed__3();
lean_mark_persistent(l_main___closed__3);
l_main___closed__4 = _init_l_main___closed__4();
lean_mark_persistent(l_main___closed__4);
return lean_io_result_mk_ok(lean_box(0));
}
void lean_initialize_runtime_module();

  #if defined(WIN32) || defined(_WIN32)
  #include <windows.h>
  #endif

  int main(int argc, char ** argv) {
  #if defined(WIN32) || defined(_WIN32)
  SetErrorMode(SEM_FAILCRITICALERRORS);
  SetConsoleOutputCP(CP_UTF8);
  #endif
  lean_object* in; lean_object* res;
lean_initialize_runtime_module();
lean_set_panic_messages(false);
res = initialize_Main(1 /* builtin */, lean_io_mk_world());
lean_set_panic_messages(true);
lean_io_mark_end_initialization();
if (lean_io_result_is_ok(res)) {
lean_dec_ref(res);
lean_init_task_manager();
res = _lean_main(lean_io_mk_world());
}
lean_finalize_task_manager();
if (lean_io_result_is_ok(res)) {
  int ret = 0;
  lean_dec_ref(res);
  return ret;
} else {
  lean_io_result_show_error(res);
  lean_dec_ref(res);
  return 1;
}
}
#ifdef __cplusplus
}
#endif
