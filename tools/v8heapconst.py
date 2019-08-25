# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  26: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  32: "STRING_TYPE",
  33: "CONS_STRING_TYPE",
  34: "EXTERNAL_STRING_TYPE",
  35: "SLICED_STRING_TYPE",
  37: "THIN_STRING_TYPE",
  40: "ONE_BYTE_STRING_TYPE",
  41: "CONS_ONE_BYTE_STRING_TYPE",
  42: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  43: "SLICED_ONE_BYTE_STRING_TYPE",
  45: "THIN_ONE_BYTE_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_STRING_TYPE",
  58: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  64: "SYMBOL_TYPE",
  65: "HEAP_NUMBER_TYPE",
  66: "BIGINT_TYPE",
  67: "ODDBALL_TYPE",
  68: "MAP_TYPE",
  69: "CODE_TYPE",
  70: "FOREIGN_TYPE",
  71: "BYTE_ARRAY_TYPE",
  72: "BYTECODE_ARRAY_TYPE",
  73: "FREE_SPACE_TYPE",
  74: "FIXED_DOUBLE_ARRAY_TYPE",
  75: "FEEDBACK_METADATA_TYPE",
  76: "FILLER_TYPE",
  77: "ACCESS_CHECK_INFO_TYPE",
  78: "ACCESSOR_INFO_TYPE",
  79: "ACCESSOR_PAIR_TYPE",
  80: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  81: "ALLOCATION_MEMENTO_TYPE",
  82: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  83: "ASM_WASM_DATA_TYPE",
  84: "ASYNC_GENERATOR_REQUEST_TYPE",
  85: "CLASS_POSITIONS_TYPE",
  86: "DEBUG_INFO_TYPE",
  87: "ENUM_CACHE_TYPE",
  88: "FUNCTION_TEMPLATE_INFO_TYPE",
  89: "FUNCTION_TEMPLATE_RARE_DATA_TYPE",
  90: "INTERCEPTOR_INFO_TYPE",
  91: "INTERPRETER_DATA_TYPE",
  92: "OBJECT_TEMPLATE_INFO_TYPE",
  93: "PROMISE_CAPABILITY_TYPE",
  94: "PROMISE_REACTION_TYPE",
  95: "PROTOTYPE_INFO_TYPE",
  96: "SCRIPT_TYPE",
  97: "SOURCE_POSITION_TABLE_WITH_FRAME_CACHE_TYPE",
  98: "SOURCE_TEXT_MODULE_INFO_ENTRY_TYPE",
  99: "STACK_FRAME_INFO_TYPE",
  100: "STACK_TRACE_FRAME_TYPE",
  101: "TEMPLATE_OBJECT_DESCRIPTION_TYPE",
  102: "TUPLE2_TYPE",
  103: "TUPLE3_TYPE",
  104: "WASM_CAPI_FUNCTION_DATA_TYPE",
  105: "WASM_DEBUG_INFO_TYPE",
  106: "WASM_EXCEPTION_TAG_TYPE",
  107: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  108: "WASM_INDIRECT_FUNCTION_TABLE_TYPE",
  109: "WASM_JS_FUNCTION_DATA_TYPE",
  110: "CALLABLE_TASK_TYPE",
  111: "CALLBACK_TASK_TYPE",
  112: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  113: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  114: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  115: "INTERNAL_CLASS_TYPE",
  116: "SMI_PAIR_TYPE",
  117: "SMI_BOX_TYPE",
  118: "SORT_STATE_TYPE",
  119: "SOURCE_TEXT_MODULE_TYPE",
  120: "SYNTHETIC_MODULE_TYPE",
  121: "ALLOCATION_SITE_TYPE",
  122: "EMBEDDER_DATA_ARRAY_TYPE",
  123: "FIXED_ARRAY_TYPE",
  124: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  125: "CLOSURE_FEEDBACK_CELL_ARRAY_TYPE",
  126: "HASH_TABLE_TYPE",
  127: "ORDERED_HASH_MAP_TYPE",
  128: "ORDERED_HASH_SET_TYPE",
  129: "ORDERED_NAME_DICTIONARY_TYPE",
  130: "NAME_DICTIONARY_TYPE",
  131: "GLOBAL_DICTIONARY_TYPE",
  132: "NUMBER_DICTIONARY_TYPE",
  133: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  134: "STRING_TABLE_TYPE",
  135: "EPHEMERON_HASH_TABLE_TYPE",
  136: "SCOPE_INFO_TYPE",
  137: "SCRIPT_CONTEXT_TABLE_TYPE",
  138: "AWAIT_CONTEXT_TYPE",
  139: "BLOCK_CONTEXT_TYPE",
  140: "CATCH_CONTEXT_TYPE",
  141: "DEBUG_EVALUATE_CONTEXT_TYPE",
  142: "EVAL_CONTEXT_TYPE",
  143: "FUNCTION_CONTEXT_TYPE",
  144: "MODULE_CONTEXT_TYPE",
  145: "NATIVE_CONTEXT_TYPE",
  146: "SCRIPT_CONTEXT_TYPE",
  147: "WITH_CONTEXT_TYPE",
  148: "WEAK_FIXED_ARRAY_TYPE",
  149: "TRANSITION_ARRAY_TYPE",
  150: "CALL_HANDLER_INFO_TYPE",
  151: "CELL_TYPE",
  152: "CODE_DATA_CONTAINER_TYPE",
  153: "DESCRIPTOR_ARRAY_TYPE",
  154: "FEEDBACK_CELL_TYPE",
  155: "FEEDBACK_VECTOR_TYPE",
  156: "LOAD_HANDLER_TYPE",
  157: "PREPARSE_DATA_TYPE",
  158: "PROPERTY_ARRAY_TYPE",
  159: "PROPERTY_CELL_TYPE",
  160: "SHARED_FUNCTION_INFO_TYPE",
  161: "SMALL_ORDERED_HASH_MAP_TYPE",
  162: "SMALL_ORDERED_HASH_SET_TYPE",
  163: "SMALL_ORDERED_NAME_DICTIONARY_TYPE",
  164: "STORE_HANDLER_TYPE",
  165: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_TYPE",
  166: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_TYPE",
  167: "WEAK_ARRAY_LIST_TYPE",
  168: "WEAK_CELL_TYPE",
  1024: "JS_PROXY_TYPE",
  1025: "JS_GLOBAL_OBJECT_TYPE",
  1026: "JS_GLOBAL_PROXY_TYPE",
  1027: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_PRIMITIVE_WRAPPER_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1057: "JS_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_TYPE",
  1059: "JS_ARRAY_BUFFER_TYPE",
  1060: "JS_ARRAY_ITERATOR_TYPE",
  1061: "JS_ARRAY_TYPE",
  1062: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1063: "JS_ASYNC_FUNCTION_OBJECT_TYPE",
  1064: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1065: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1066: "JS_DATE_TYPE",
  1067: "JS_ERROR_TYPE",
  1068: "JS_GENERATOR_OBJECT_TYPE",
  1069: "JS_MAP_TYPE",
  1070: "JS_MAP_KEY_ITERATOR_TYPE",
  1071: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1072: "JS_MAP_VALUE_ITERATOR_TYPE",
  1073: "JS_MESSAGE_OBJECT_TYPE",
  1074: "JS_PROMISE_TYPE",
  1075: "JS_REGEXP_TYPE",
  1076: "JS_REGEXP_STRING_ITERATOR_TYPE",
  1077: "JS_SET_TYPE",
  1078: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1079: "JS_SET_VALUE_ITERATOR_TYPE",
  1080: "JS_STRING_ITERATOR_TYPE",
  1081: "JS_WEAK_REF_TYPE",
  1082: "JS_FINALIZATION_GROUP_CLEANUP_ITERATOR_TYPE",
  1083: "JS_FINALIZATION_GROUP_TYPE",
  1084: "JS_WEAK_MAP_TYPE",
  1085: "JS_WEAK_SET_TYPE",
  1086: "JS_TYPED_ARRAY_TYPE",
  1087: "JS_DATA_VIEW_TYPE",
  1088: "JS_INTL_V8_BREAK_ITERATOR_TYPE",
  1089: "JS_INTL_COLLATOR_TYPE",
  1090: "JS_INTL_DATE_TIME_FORMAT_TYPE",
  1091: "JS_INTL_LIST_FORMAT_TYPE",
  1092: "JS_INTL_LOCALE_TYPE",
  1093: "JS_INTL_NUMBER_FORMAT_TYPE",
  1094: "JS_INTL_PLURAL_RULES_TYPE",
  1095: "JS_INTL_RELATIVE_TIME_FORMAT_TYPE",
  1096: "JS_INTL_SEGMENT_ITERATOR_TYPE",
  1097: "JS_INTL_SEGMENTER_TYPE",
  1098: "WASM_EXCEPTION_TYPE",
  1099: "WASM_GLOBAL_TYPE",
  1100: "WASM_INSTANCE_TYPE",
  1101: "WASM_MEMORY_TYPE",
  1102: "WASM_MODULE_TYPE",
  1103: "WASM_TABLE_TYPE",
  1104: "JS_BOUND_FUNCTION_TYPE",
  1105: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("read_only_space", 0x00111): (73, "FreeSpaceMap"),
  ("read_only_space", 0x00161): (68, "MetaMap"),
  ("read_only_space", 0x001e1): (67, "NullMap"),
  ("read_only_space", 0x00249): (153, "DescriptorArrayMap"),
  ("read_only_space", 0x002a9): (148, "WeakFixedArrayMap"),
  ("read_only_space", 0x002f9): (76, "OnePointerFillerMap"),
  ("read_only_space", 0x00349): (76, "TwoPointerFillerMap"),
  ("read_only_space", 0x003c9): (67, "UninitializedMap"),
  ("read_only_space", 0x00439): (8, "OneByteInternalizedStringMap"),
  ("read_only_space", 0x004d9): (67, "UndefinedMap"),
  ("read_only_space", 0x00539): (65, "HeapNumberMap"),
  ("read_only_space", 0x005b9): (67, "TheHoleMap"),
  ("read_only_space", 0x00661): (67, "BooleanMap"),
  ("read_only_space", 0x00739): (71, "ByteArrayMap"),
  ("read_only_space", 0x00789): (123, "FixedArrayMap"),
  ("read_only_space", 0x007d9): (123, "FixedCOWArrayMap"),
  ("read_only_space", 0x00829): (126, "HashTableMap"),
  ("read_only_space", 0x00879): (64, "SymbolMap"),
  ("read_only_space", 0x008c9): (40, "OneByteStringMap"),
  ("read_only_space", 0x00919): (136, "ScopeInfoMap"),
  ("read_only_space", 0x00969): (160, "SharedFunctionInfoMap"),
  ("read_only_space", 0x009b9): (69, "CodeMap"),
  ("read_only_space", 0x00a09): (143, "FunctionContextMap"),
  ("read_only_space", 0x00a59): (151, "CellMap"),
  ("read_only_space", 0x00aa9): (159, "GlobalPropertyCellMap"),
  ("read_only_space", 0x00af9): (70, "ForeignMap"),
  ("read_only_space", 0x00b49): (149, "TransitionArrayMap"),
  ("read_only_space", 0x00b99): (155, "FeedbackVectorMap"),
  ("read_only_space", 0x00c39): (67, "ArgumentsMarkerMap"),
  ("read_only_space", 0x00cd9): (67, "ExceptionMap"),
  ("read_only_space", 0x00d79): (67, "TerminationExceptionMap"),
  ("read_only_space", 0x00e21): (67, "OptimizedOutMap"),
  ("read_only_space", 0x00ec1): (67, "StaleRegisterMap"),
  ("read_only_space", 0x00f31): (145, "NativeContextMap"),
  ("read_only_space", 0x00f81): (144, "ModuleContextMap"),
  ("read_only_space", 0x00fd1): (142, "EvalContextMap"),
  ("read_only_space", 0x01021): (146, "ScriptContextMap"),
  ("read_only_space", 0x01071): (138, "AwaitContextMap"),
  ("read_only_space", 0x010c1): (139, "BlockContextMap"),
  ("read_only_space", 0x01111): (140, "CatchContextMap"),
  ("read_only_space", 0x01161): (147, "WithContextMap"),
  ("read_only_space", 0x011b1): (141, "DebugEvaluateContextMap"),
  ("read_only_space", 0x01201): (137, "ScriptContextTableMap"),
  ("read_only_space", 0x01251): (125, "ClosureFeedbackCellArrayMap"),
  ("read_only_space", 0x012a1): (75, "FeedbackMetadataArrayMap"),
  ("read_only_space", 0x012f1): (123, "ArrayListMap"),
  ("read_only_space", 0x01341): (66, "BigIntMap"),
  ("read_only_space", 0x01391): (124, "ObjectBoilerplateDescriptionMap"),
  ("read_only_space", 0x013e1): (72, "BytecodeArrayMap"),
  ("read_only_space", 0x01431): (152, "CodeDataContainerMap"),
  ("read_only_space", 0x01481): (74, "FixedDoubleArrayMap"),
  ("read_only_space", 0x014d1): (131, "GlobalDictionaryMap"),
  ("read_only_space", 0x01521): (154, "ManyClosuresCellMap"),
  ("read_only_space", 0x01571): (123, "ModuleInfoMap"),
  ("read_only_space", 0x015c1): (130, "NameDictionaryMap"),
  ("read_only_space", 0x01611): (154, "NoClosuresCellMap"),
  ("read_only_space", 0x01661): (132, "NumberDictionaryMap"),
  ("read_only_space", 0x016b1): (154, "OneClosureCellMap"),
  ("read_only_space", 0x01701): (127, "OrderedHashMapMap"),
  ("read_only_space", 0x01751): (128, "OrderedHashSetMap"),
  ("read_only_space", 0x017a1): (129, "OrderedNameDictionaryMap"),
  ("read_only_space", 0x017f1): (157, "PreparseDataMap"),
  ("read_only_space", 0x01841): (158, "PropertyArrayMap"),
  ("read_only_space", 0x01891): (150, "SideEffectCallHandlerInfoMap"),
  ("read_only_space", 0x018e1): (150, "SideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x01931): (150, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x01981): (133, "SimpleNumberDictionaryMap"),
  ("read_only_space", 0x019d1): (123, "SloppyArgumentsElementsMap"),
  ("read_only_space", 0x01a21): (161, "SmallOrderedHashMapMap"),
  ("read_only_space", 0x01a71): (162, "SmallOrderedHashSetMap"),
  ("read_only_space", 0x01ac1): (163, "SmallOrderedNameDictionaryMap"),
  ("read_only_space", 0x01b11): (119, "SourceTextModuleMap"),
  ("read_only_space", 0x01b61): (134, "StringTableMap"),
  ("read_only_space", 0x01bb1): (120, "SyntheticModuleMap"),
  ("read_only_space", 0x01c01): (165, "UncompiledDataWithoutPreparseDataMap"),
  ("read_only_space", 0x01c51): (166, "UncompiledDataWithPreparseDataMap"),
  ("read_only_space", 0x01ca1): (167, "WeakArrayListMap"),
  ("read_only_space", 0x01cf1): (135, "EphemeronHashTableMap"),
  ("read_only_space", 0x01d41): (122, "EmbedderDataArrayMap"),
  ("read_only_space", 0x01d91): (168, "WeakCellMap"),
  ("read_only_space", 0x01de1): (58, "NativeSourceStringMap"),
  ("read_only_space", 0x01e31): (32, "StringMap"),
  ("read_only_space", 0x01e81): (41, "ConsOneByteStringMap"),
  ("read_only_space", 0x01ed1): (33, "ConsStringMap"),
  ("read_only_space", 0x01f21): (45, "ThinOneByteStringMap"),
  ("read_only_space", 0x01f71): (37, "ThinStringMap"),
  ("read_only_space", 0x01fc1): (35, "SlicedStringMap"),
  ("read_only_space", 0x02011): (43, "SlicedOneByteStringMap"),
  ("read_only_space", 0x02061): (34, "ExternalStringMap"),
  ("read_only_space", 0x020b1): (42, "ExternalOneByteStringMap"),
  ("read_only_space", 0x02101): (50, "UncachedExternalStringMap"),
  ("read_only_space", 0x02151): (0, "InternalizedStringMap"),
  ("read_only_space", 0x021a1): (2, "ExternalInternalizedStringMap"),
  ("read_only_space", 0x021f1): (10, "ExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x02241): (18, "UncachedExternalInternalizedStringMap"),
  ("read_only_space", 0x02291): (26, "UncachedExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x022e1): (58, "UncachedExternalOneByteStringMap"),
  ("read_only_space", 0x02331): (67, "SelfReferenceMarkerMap"),
  ("read_only_space", 0x02399): (87, "EnumCacheMap"),
  ("read_only_space", 0x02439): (82, "ArrayBoilerplateDescriptionMap"),
  ("read_only_space", 0x02629): (90, "InterceptorInfoMap"),
  ("read_only_space", 0x04ea9): (77, "AccessCheckInfoMap"),
  ("read_only_space", 0x04ef9): (78, "AccessorInfoMap"),
  ("read_only_space", 0x04f49): (79, "AccessorPairMap"),
  ("read_only_space", 0x04f99): (80, "AliasedArgumentsEntryMap"),
  ("read_only_space", 0x04fe9): (81, "AllocationMementoMap"),
  ("read_only_space", 0x05039): (83, "AsmWasmDataMap"),
  ("read_only_space", 0x05089): (84, "AsyncGeneratorRequestMap"),
  ("read_only_space", 0x050d9): (85, "ClassPositionsMap"),
  ("read_only_space", 0x05129): (86, "DebugInfoMap"),
  ("read_only_space", 0x05179): (88, "FunctionTemplateInfoMap"),
  ("read_only_space", 0x051c9): (89, "FunctionTemplateRareDataMap"),
  ("read_only_space", 0x05219): (91, "InterpreterDataMap"),
  ("read_only_space", 0x05269): (92, "ObjectTemplateInfoMap"),
  ("read_only_space", 0x052b9): (93, "PromiseCapabilityMap"),
  ("read_only_space", 0x05309): (94, "PromiseReactionMap"),
  ("read_only_space", 0x05359): (95, "PrototypeInfoMap"),
  ("read_only_space", 0x053a9): (96, "ScriptMap"),
  ("read_only_space", 0x053f9): (97, "SourcePositionTableWithFrameCacheMap"),
  ("read_only_space", 0x05449): (98, "SourceTextModuleInfoEntryMap"),
  ("read_only_space", 0x05499): (99, "StackFrameInfoMap"),
  ("read_only_space", 0x054e9): (100, "StackTraceFrameMap"),
  ("read_only_space", 0x05539): (101, "TemplateObjectDescriptionMap"),
  ("read_only_space", 0x05589): (102, "Tuple2Map"),
  ("read_only_space", 0x055d9): (103, "Tuple3Map"),
  ("read_only_space", 0x05629): (104, "WasmCapiFunctionDataMap"),
  ("read_only_space", 0x05679): (105, "WasmDebugInfoMap"),
  ("read_only_space", 0x056c9): (106, "WasmExceptionTagMap"),
  ("read_only_space", 0x05719): (107, "WasmExportedFunctionDataMap"),
  ("read_only_space", 0x05769): (108, "WasmIndirectFunctionTableMap"),
  ("read_only_space", 0x057b9): (109, "WasmJSFunctionDataMap"),
  ("read_only_space", 0x05809): (110, "CallableTaskMap"),
  ("read_only_space", 0x05859): (111, "CallbackTaskMap"),
  ("read_only_space", 0x058a9): (112, "PromiseFulfillReactionJobTaskMap"),
  ("read_only_space", 0x058f9): (113, "PromiseRejectReactionJobTaskMap"),
  ("read_only_space", 0x05949): (114, "PromiseResolveThenableJobTaskMap"),
  ("read_only_space", 0x05999): (115, "InternalClassMap"),
  ("read_only_space", 0x059e9): (116, "SmiPairMap"),
  ("read_only_space", 0x05a39): (117, "SmiBoxMap"),
  ("read_only_space", 0x05a89): (118, "SortStateMap"),
  ("read_only_space", 0x05ad9): (121, "AllocationSiteWithWeakNextMap"),
  ("read_only_space", 0x05b29): (121, "AllocationSiteWithoutWeakNextMap"),
  ("read_only_space", 0x05b79): (156, "LoadHandler1Map"),
  ("read_only_space", 0x05bc9): (156, "LoadHandler2Map"),
  ("read_only_space", 0x05c19): (156, "LoadHandler3Map"),
  ("read_only_space", 0x05c69): (164, "StoreHandler0Map"),
  ("read_only_space", 0x05cb9): (164, "StoreHandler1Map"),
  ("read_only_space", 0x05d09): (164, "StoreHandler2Map"),
  ("read_only_space", 0x05d59): (164, "StoreHandler3Map"),
  ("map_space", 0x00111): (1057, "ExternalMap"),
  ("map_space", 0x00161): (1073, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("read_only_space", 0x001b1): "NullValue",
  ("read_only_space", 0x00231): "EmptyDescriptorArray",
  ("read_only_space", 0x00299): "EmptyWeakFixedArray",
  ("read_only_space", 0x00399): "UninitializedValue",
  ("read_only_space", 0x004a9): "UndefinedValue",
  ("read_only_space", 0x00529): "NanValue",
  ("read_only_space", 0x00589): "TheHoleValue",
  ("read_only_space", 0x00621): "HoleNanValue",
  ("read_only_space", 0x00631): "TrueValue",
  ("read_only_space", 0x006e1): "FalseValue",
  ("read_only_space", 0x00729): "empty_string",
  ("read_only_space", 0x00be9): "EmptyScopeInfo",
  ("read_only_space", 0x00bf9): "EmptyFixedArray",
  ("read_only_space", 0x00c09): "ArgumentsMarker",
  ("read_only_space", 0x00ca9): "Exception",
  ("read_only_space", 0x00d49): "TerminationException",
  ("read_only_space", 0x00df1): "OptimizedOut",
  ("read_only_space", 0x00e91): "StaleRegister",
  ("read_only_space", 0x02381): "EmptyEnumCache",
  ("read_only_space", 0x023e9): "EmptyPropertyArray",
  ("read_only_space", 0x023f9): "EmptyByteArray",
  ("read_only_space", 0x02409): "EmptyObjectBoilerplateDescription",
  ("read_only_space", 0x02421): "EmptyArrayBoilerplateDescription",
  ("read_only_space", 0x02489): "EmptyClosureFeedbackCellArray",
  ("read_only_space", 0x02499): "EmptySloppyArgumentsElements",
  ("read_only_space", 0x024b9): "EmptySlowElementDictionary",
  ("read_only_space", 0x02501): "EmptyOrderedHashMap",
  ("read_only_space", 0x02529): "EmptyOrderedHashSet",
  ("read_only_space", 0x02551): "EmptyFeedbackMetadata",
  ("read_only_space", 0x02561): "EmptyPropertyCell",
  ("read_only_space", 0x02589): "EmptyPropertyDictionary",
  ("read_only_space", 0x025d9): "NoOpInterceptorInfo",
  ("read_only_space", 0x02679): "EmptyWeakArrayList",
  ("read_only_space", 0x02691): "InfinityValue",
  ("read_only_space", 0x026a1): "MinusZeroValue",
  ("read_only_space", 0x026b1): "MinusInfinityValue",
  ("read_only_space", 0x026c1): "SelfReferenceMarker",
  ("read_only_space", 0x02719): "OffHeapTrampolineRelocationInfo",
  ("read_only_space", 0x02731): "TrampolineTrivialCodeDataContainer",
  ("read_only_space", 0x02749): "TrampolinePromiseRejectionCodeDataContainer",
  ("read_only_space", 0x02761): "GlobalThisBindingScopeInfo",
  ("read_only_space", 0x027c9): "EmptyFunctionScopeInfo",
  ("read_only_space", 0x02819): "HashSeed",
  ("old_space", 0x00111): "ArgumentsIteratorAccessor",
  ("old_space", 0x00181): "ArrayLengthAccessor",
  ("old_space", 0x001f1): "BoundFunctionLengthAccessor",
  ("old_space", 0x00261): "BoundFunctionNameAccessor",
  ("old_space", 0x002d1): "ErrorStackAccessor",
  ("old_space", 0x00341): "FunctionArgumentsAccessor",
  ("old_space", 0x003b1): "FunctionCallerAccessor",
  ("old_space", 0x00421): "FunctionNameAccessor",
  ("old_space", 0x00491): "FunctionLengthAccessor",
  ("old_space", 0x00501): "FunctionPrototypeAccessor",
  ("old_space", 0x00571): "StringLengthAccessor",
  ("old_space", 0x005e1): "InvalidPrototypeValidityCell",
  ("old_space", 0x005f1): "EmptyScript",
  ("old_space", 0x00671): "ManyClosuresCell",
  ("old_space", 0x00689): "ArrayConstructorProtector",
  ("old_space", 0x00699): "NoElementsProtector",
  ("old_space", 0x006c1): "IsConcatSpreadableProtector",
  ("old_space", 0x006d1): "ArraySpeciesProtector",
  ("old_space", 0x006f9): "TypedArraySpeciesProtector",
  ("old_space", 0x00721): "PromiseSpeciesProtector",
  ("old_space", 0x00749): "StringLengthProtector",
  ("old_space", 0x00759): "ArrayIteratorProtector",
  ("old_space", 0x00781): "ArrayBufferDetachingProtector",
  ("old_space", 0x007a9): "PromiseHookProtector",
  ("old_space", 0x007d1): "PromiseResolveProtector",
  ("old_space", 0x007e1): "MapIteratorProtector",
  ("old_space", 0x00809): "PromiseThenProtector",
  ("old_space", 0x00831): "SetIteratorProtector",
  ("old_space", 0x00859): "StringIteratorProtector",
  ("old_space", 0x00881): "SingleCharacterStringCache",
  ("old_space", 0x01091): "StringSplitCache",
  ("old_space", 0x018a1): "RegExpMultipleCache",
  ("old_space", 0x020b1): "BuiltinsConstantsTable",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM_COMPILED",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_INTERPRETER_ENTRY",
  "C_WASM_ENTRY",
  "WASM_EXIT",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
