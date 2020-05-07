/*
Based on the shader code given in the Arnold doc "Creating a Shader".
	https://docs.arnoldrenderer.com/display/AFMUG/Creating+a+shader#CreatingaShader-1.1.1InstallingaC++Compiler 
Malcolm Kesson
Aug 17 2019
*/
#include <ai.h>
#include <cstring>

AI_SHADER_NODE_EXPORT_METHODS(SampleMethods);
 AtRGB mix(AtRGB c1, AtRGB c2, float alpha) {
	return c1 * (1.0 - alpha) + c2 * alpha;
	}
 
namespace {
	enum paramIndex { k_rear_color, k_front_color, k_swap };
	};
	
node_parameters {
    AiParameterRGB("rearColor", 0.7f, 0.7f, 0);
    AiParameterRGB("frontColor", 0.7f, 0, 0);
	AiParameterBool("swap", 0);
	}
 
shader_evaluate {
	AtRGB rearColor = AiShaderEvalParamRGB(k_rear_color);
	AtRGB frontColor = AiShaderEvalParamRGB(k_front_color);
	bool swap = AiShaderEvalParamBool(k_swap);
	
	
			if(sg->N == sg->Nf) 
				sg->out.RGB() = (swap) ? rearColor : frontColor;
			else
				sg->out.RGB() = (swap) ? frontColor: rearColor;
			}		
			
node_loader {
    if (i > 0)
        return false; 
    node->methods        = SampleMethods;
    node->output_type    = AI_TYPE_RGB;
	node->name           = "tkSideMask";
    node->node_type      = AI_NODE_SHADER;
    strcpy(node->version, AI_VERSION);
    return true;
	}
	
// The remaining macros can be left "empty"
node_initialize { }
node_update { }
node_finish { }
